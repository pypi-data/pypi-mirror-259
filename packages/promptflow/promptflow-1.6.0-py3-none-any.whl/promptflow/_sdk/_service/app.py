# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import logging
import sys
import time
from datetime import datetime, timedelta
from logging.handlers import RotatingFileHandler

from flask import Blueprint, Flask, g, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from promptflow._sdk._constants import PF_SERVICE_HOUR_TIMEOUT, PF_SERVICE_LOG_FILE, PF_SERVICE_MONITOR_SECOND
from promptflow._sdk._service import Api
from promptflow._sdk._service.apis.collector import trace_collector
from promptflow._sdk._service.apis.connection import api as connection_api
from promptflow._sdk._service.apis.line_run import api as line_run_api
from promptflow._sdk._service.apis.run import api as run_api
from promptflow._sdk._service.apis.span import api as span_api
from promptflow._sdk._service.apis.telemetry import api as telemetry_api
from promptflow._sdk._service.apis.ui import api as ui_api
from promptflow._sdk._service.utils.utils import (
    FormattedException,
    get_current_env_pfs_file,
    get_port_from_config,
    kill_exist_service,
)
from promptflow._sdk._utils import get_promptflow_sdk_version, overwrite_null_std_logger
from promptflow._utils.thread_utils import ThreadWithContextVars

overwrite_null_std_logger()


def heartbeat():
    response = {"promptflow": get_promptflow_sdk_version()}
    return jsonify(response)


def create_app():
    app = Flask(__name__)

    # in normal case, we don't need to handle CORS for PFS
    # as far as we know, local UX development might need to handle this
    # as there might be different ports in that scenario
    CORS(app)

    app.add_url_rule("/heartbeat", view_func=heartbeat)
    app.add_url_rule("/v1/traces", view_func=trace_collector, methods=["POST"])
    with app.app_context():
        api_v1 = Blueprint("Prompt Flow Service", __name__, url_prefix="/v1.0")

        # Registers resources from namespace for current instance of api
        api = Api(api_v1, title="Prompt Flow Service", version="1.0")
        api.add_namespace(connection_api)
        api.add_namespace(run_api)
        api.add_namespace(telemetry_api)
        api.add_namespace(span_api)
        api.add_namespace(line_run_api)
        api.add_namespace(ui_api)
        app.register_blueprint(api_v1)

        # Disable flask-restx set X-Fields in header. https://flask-restx.readthedocs.io/en/latest/mask.html#usage
        app.config["RESTX_MASK_SWAGGER"] = False

        # Enable log
        app.logger.setLevel(logging.INFO)
        # each env will have its own log file
        log_file = get_current_env_pfs_file(PF_SERVICE_LOG_FILE)
        # Create a rotating file handler with a max size of 1 MB and keeping up to 1 backup files
        handler = RotatingFileHandler(filename=log_file, maxBytes=1_000_000, backupCount=1)
        formatter = logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s] - %(message)s")
        handler.setFormatter(formatter)
        # Set app logger to the only one RotatingFileHandler to avoid duplicate logs
        app.logger.handlers = [handler]

        # Basic error handler
        @api.errorhandler(Exception)
        def handle_exception(e):
            """When any error occurs on the server, return a formatted error message."""
            from dataclasses import asdict

            if isinstance(e, HTTPException):
                return asdict(FormattedException(e), dict_factory=lambda x: {k: v for (k, v) in x if v}), e.code
            app.logger.error(e, exc_info=True, stack_info=True)
            formatted_exception = FormattedException(e)
            return (
                asdict(formatted_exception, dict_factory=lambda x: {k: v for (k, v) in x if v}),
                formatted_exception.status_code,
            )

        @app.before_request
        def log_before_request_info():
            app.config["last_request_time"] = datetime.now()
            g.start = time.perf_counter()
            if "/v1.0/Connections" in request.url:
                request_body = "Request body not recorded for Connections API"
            else:
                request_body = request.get_data()

            app.logger.debug(
                "Last request time: %s, Headers: %s, Body: %s",
                app.config["last_request_time"],
                request.headers,
                request_body,
            )

        @app.after_request
        def log_after_request_info(response):
            duration_time = time.perf_counter() - g.start
            app.logger.info(
                "Request_url: %s, duration: %s, response code: %s", request.url, duration_time, response.status_code
            )
            return response

        # Start a monitor process using detach mode. It will stop pfs service if no request to pfs service in 1h in
        # python scenario. For C# scenario, pfs will live until the process is killed manually.
        def monitor_request():
            while True:
                time.sleep(PF_SERVICE_MONITOR_SECOND)
                if "last_request_time" in app.config and datetime.now() - app.config["last_request_time"] > timedelta(
                    hours=PF_SERVICE_HOUR_TIMEOUT
                ):
                    # Todo: check if we have any not complete work? like persist all traces.
                    port = get_port_from_config()
                    if port:
                        app.logger.info(f"Try auto stop pfs service in port {port} since no request to app within 1h")
                        kill_exist_service(port)
                    break

        if not sys.executable.endswith("pfcli.exe"):
            monitor_thread = ThreadWithContextVars(target=monitor_request, daemon=True)
            monitor_thread.start()
    return app, api
