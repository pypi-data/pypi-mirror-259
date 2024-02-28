from threading import Event  # Ensure this import is at the top of your file
import json
import os
import tempfile
import zipfile
from typing import List, Union, Optional, Dict, Any
import jwt
from datetime import datetime
import yaml
import re

import requests
from enum import Enum
from tenacity import retry, stop_after_delay, wait_fixed
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper
import time
from cerebrium import datatypes, sync_files

import cerebrium.utils as utils
import cerebrium.logging as logging


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"


env = os.getenv("ENV", "prod")

dashboard_url = (
    os.environ["DASHBOARD_URL"]
    if "DASHBOARD_URL" in os.environ
    else (
        "https://dev-dashboard.cerebrium.ai"
        if env == "dev"
        else "https://dashboard.cerebrium.ai"
    )
)

api_url = (
    os.environ["REST_API_URL"]
    if "REST_API_URL" in os.environ
    else (
        "https://dev-rest-api.cerebrium.ai"
        if env == "dev"
        else (
            "http://localhost:4100"
            if env == "local"
            else "https://rest-api.cerebrium.ai"
        )
    )
)

client_id = (
    os.environ["CLIENT_ID"]
    if "CLIENT_ID" in os.environ
    else (
        "207hg1caksrebuc79pcq1r3269"
        if env in ["dev", "local"]
        else "2om0uempl69t4c6fc70ujstsuk"
    )
)

auth_url = (
    os.environ["AUTH_URL"]
    if "AUTH_URL" in os.environ
    else (
        "https://dev-cerebrium.auth.eu-west-1.amazoncognito.com/oauth2/token"
        if env in ["dev", "local"]
        else "https://prod-cerebrium.auth.eu-west-1.amazoncognito.com/oauth2/token"
    )
)

stream_logs_url = (
    os.environ["STREAM_LOGS_URL"]
    if "STREAM_LOGS_URL" in os.environ
    else (
        "https://gklwrtbtdgb4fvs72bw5j2ap3q0omics.lambda-url.eu-west-1.on.aws"
        if env == "dev"
        else "https://icnl4trzmhm422rmqbyp4pgniq0uresm.lambda-url.eu-west-1.on.aws"
    )
)


def is_logged_in():
    """
    Check if a user's JWT token has expired. If it has, make a request to Cognito with the refresh token to generate a new one.

    Returns:
        str: The new JWT token if the old one has expired, otherwise the current JWT token.
    """
    # Assuming the JWT token is stored in a config file
    config_path = os.path.expanduser("~/.cerebrium/config.yaml")
    if not os.path.exists(config_path):
        logging.cerebrium_log(
            level="ERROR",
            message="You must log in to use this functionality. Please run 'cerebrium login'",
            prefix="",
        )
        return False

    with open(config_path, "r") as f:
        config = yaml.safe_load(f) or {}

    if config is None:
        logging.cerebrium_log(
            level="ERROR",
            message="You must log in to use this functionality. Please run 'cerebrium login'",
            prefix="",
        )
        return False

    key_name = ""
    if env == "dev":
        key_name = "dev-"
    elif env == "local":
        key_name = "local-"

    jwt_token = config.get(f"{key_name}accessToken")
    refresh_token = config.get(f"{key_name}refreshToken")
    if not jwt_token:
        logging.cerebrium_log(
            level="ERROR",
            message="You must log in to use this functionality. Please run 'cerebrium login'",
            prefix="",
        )
        return False

    # Decode the JWT token without verification to check the expiration time
    try:
        payload = jwt.decode(jwt_token, options={"verify_signature": False})
    except Exception as e:
        logging.cerebrium_log(
            level="ERROR", message=f"Failed to decode JWT token: {str(e)}", prefix=""
        )
        return None  # Check if the token has expired
    if datetime.fromtimestamp(payload["exp"]) < datetime.now():
        # Token has expired, request a new one using the refresh token
        response = requests.post(
            auth_url,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "refresh_token",
                "client_id": client_id,
                "refresh_token": refresh_token,
            },
        )
        if response.status_code == 200:
            new_jwt_token = response.json()["access_token"]
            # Update the config file with the new JWT token
            config[f"{key_name}accessToken"] = new_jwt_token
            with open(config_path, "w") as f:
                yaml.safe_dump(config, f)
            return new_jwt_token
        else:
            logging.cerebrium_log(
                level="ERROR",
                message="Failed to refresh JWT token. Please login again.",
                prefix="",
            )
            return False
    else:
        # Token has not expired, return the current JWT token
        return jwt_token


def cerebrium_request(
    http_method: HttpMethod,
    url: str,
    payload: Optional[Dict[str, Any]] = None,
    requires_auth: bool = True,
    stream: bool = False,
    custom_headers: Optional[Dict[str, Any]] = None,
) -> Union[requests.Response, None]:
    """
    Make a request to the Cerebrium API and check the response for errors.

    Args:
        http_method (HttpMethod): The HTTP method to use (GET, POST or DELETE).
        url (str): The url after the base url to use.
        payload (dict, optional): The payload to send with the request.
        requires_auth (bool): If the api call requires the user to be authenticated
        steam (bool): If the request is to a streaming endpoint
        custom_headers (dict, optional): By default, content-type is application/json so this is used to override

    Returns:
        dict: The response from the request.
    """
    if requires_auth:
        access_token = is_logged_in()
        if not access_token:
            return

        current_project_id = utils.get_current_project_context()

        if payload is None:
            payload = {}
        payload["projectId"] = current_project_id
    else:
        access_token = None

    url = f"{stream_logs_url}/{url}" if stream else f"{api_url}/{url}"

    if custom_headers is not None:
        headers = custom_headers
    else:
        headers = {"ContentType": "application/json"}

    if access_token:
        headers["Authorization"] = f"{access_token}"

    @retry(stop=stop_after_delay(60), wait=wait_fixed(8))
    def _request():
        data = None if payload is None else json.dumps(payload)
        if http_method == HttpMethod.POST:
            response = requests.post(url, headers=headers, data=data, timeout=30)
        elif http_method == HttpMethod.GET:
            response = requests.get(
                url,
                headers=headers,
                params=payload,
                stream=stream,
                timeout=None if stream else 30,
            )
        else:
            response = requests.delete(
                url, headers=headers, params=payload, data=data, timeout=30
            )
        return response

    response = _request()

    return response


def get_build_status(build_id: str) -> str:
    """Get the build status of a build from the backend"""
    build_status_response = cerebrium_request(
        HttpMethod.GET, f"getBuildStatus?buildId={build_id}", {}
    )

    if build_status_response is None:
        logging.cerebrium_log(
            level="ERROR",
            message="Error getting build status. Please check your internet connection and ensure you are logged in. If this issue persists, please contact support.",
        )
        exit()

    if build_status_response.status_code != 200:
        logging.cerebrium_log(
            level="ERROR",
            message=f"Error getting build status\n{build_status_response.json()['message']}",
            prefix="",
        )

    return build_status_response.json()["status"]


def upload_cortex_files(
    upload_url: str,
    zip_file_name: str,
    config: datatypes.CerebriumConfig,
) -> bool:
    if config.file_list == []:
        logging.cerebrium_log(
            level="ERROR",
            message="No files to upload.",
            prefix="Error uploading app to Cerebrium:",
        )

    # Zip all files in the current directory and upload to S3
    with tempfile.TemporaryDirectory() as temp_dir:
        zip_path = os.path.join(temp_dir, zip_file_name)
        dir_name = os.path.dirname(zip_path)

        sync_files.make_cortex_util_files(temp_dir, config)

        os.makedirs(dir_name, exist_ok=True)

        tmp_dir_files = os.listdir(temp_dir)
        with zipfile.ZipFile(zip_path, "w") as zip_file:
            print("🗂️  Zipping files...")
            for f in config.file_list:
                if os.path.isfile(f):
                    zip_file.write(f)

            for f in datatypes.INTERNAL_FILES:
                if f in tmp_dir_files:
                    zip_file.write(
                        os.path.join(temp_dir, f), arcname=os.path.basename(f)
                    )

        print("⬆️  Uploading to Cerebrium...")
        with open(zip_path, "rb") as f:
            headers = {
                "Content-Type": "application/zip",
            }
            if not config.build.disable_animation:
                with tqdm(
                    total=os.path.getsize(zip_path),
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                    colour="#EB3A6F",
                ) as pbar:  # type: ignore
                    wrapped_f = CallbackIOWrapper(pbar.update, f, "read")
                    upload_response = requests.put(
                        upload_url,
                        headers=headers,
                        data=wrapped_f,  # type: ignore
                        timeout=60,
                        stream=True,
                    )
            else:
                upload_response = requests.put(
                    upload_url,
                    headers=headers,
                    data=f,
                    timeout=60,
                    stream=True,
                )

            if upload_response.status_code != 200:
                logging.cerebrium_log(
                    level="ERROR",
                    message="Error uploading app to Cerebrium:",
                    prefix="",
                )

            print("✅ Resources uploaded successfully.")
            return True


def log_build_status(
    build_status: str,
    start_time: float,
) -> str:
    # Status messages mapping
    status_messages = {
        "building": "🔨 Building App...",
        "initializing": "🛠️ Initializing...",
        "synchronizing_files": "📂 Syncing files...",
        "pending": "⏳ Build pending...",
        "failed": "🚨 Build failed!",
    }

    # Default message
    msg = status_messages.get(build_status, "waiting for build status...")

    if build_status == "pending" and time.time() - start_time > 20:
        msg = "⏳ Build pending...trying to find hardware"

    return msg


def stream_logs(
    start_event: Event,
    stop_event: Event,
    modelId: Optional[str] = None,
    buildId: Optional[str] = None,
):
    """

    Hits a streaming logging endpoint and prints out the logs.

    Args:
        start_event (threading event): Lets thread know that it has started receiving logs.
        stop_event (threading event): Lets thread know that it should stop processing
        modelId (str, optional): The unique identifier of the model you would like to see streamed logs for
        buildId (str, optional): The unique identifier of the build you would like to see streamed logs for
    """

    if not modelId and not buildId:
        raise ValueError("Either 'modelId' or 'buildId' must be provided.")

    try:
        custom_headers = {
            "Content-Type": "text/event-stream",
            "Transfer-Encoding": "chunked",
            "Connection": "keep-alive",
        }

        response = cerebrium_request(
            HttpMethod.GET,
            f"?modelId={modelId}&buildId={buildId}",
            {},
            custom_headers=custom_headers,
            stream=True,
        )

        if response is None:
            logging.cerebrium_log(
                level="ERROR",
                message="Error streaming logs. Please check your internet connection and ensure you are logged in. If this issue persists, please contact support.",
            )
            exit()

        if response.status_code == 200:
            for line in response.iter_lines():
                if stop_event.is_set():  # Check if the stop event is set
                    break  # Exit the loop if the stop event is set
                if line:
                    decoded_line = line.decode("utf-8")
                    logging.log_formatted_response(decoded_line)
                    if not start_event.is_set():
                        start_event.set()  #
        else:
            logging.logger.error(
                f"Failed to stream logs. Status code: {response.status_code}"
            )
    except Exception as e:
        logging.logger.error(f"An error occurred while streaming logs: {e}")


def poll_build_logs(
    buildId: str, start_event: Event, stop_event: Event, interval: int = 2
):
    """
    Polls logs at specified intervals and prints only new log lines.

    Args:
        buildId (str, optional): The unique identifier of the build you would like to see streamed logs for
        start_event (threading event): Lets thread know that it has started receiving logs.
        stop_event (threading event): Lets thread know that it should stop processing
        interval (int): The interval in seconds between polls. Defaults to 2 seconds.
    """
    last_seen_logs: List[str] = []
    while not stop_event.is_set():
        logs_response = cerebrium_request(
            HttpMethod.GET, f"streamBuildLogs?buildId={buildId}", {}
        )
        if logs_response is None:
            logging.cerebrium_log(
                level="ERROR",
                message="Error streaming logs. Please check your internet connection and ensure you are logged in. If this issue persists, please contact support.",
            )
            exit()

        if logs_response.status_code == 200:
            # Concatenate the log parts into a single string
            concatenated_logs = "".join(logs_response.json()["logs"])
            # Use a regular expression to split the concatenated string into lines at timestamps
            # Assuming ISO 8601 format for timestamps: 2024-02-05T21:12:05.650831712Z
            current_log_lines = re.split(
                r"(?=\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z)", concatenated_logs
            )

            # Process each log line
            for line in current_log_lines:
                if (
                    line and line not in last_seen_logs
                ):  # Check if the line is not in the list of seen logs
                    logging.log_formatted_response(
                        line
                    )  # we should always receive some type of log so wait until this happens
                    start_event.set()
                    last_seen_logs.append(
                        line
                    )  # Add the new line to the list of seen logs

        else:
            print(f"Failed to fetch logs. Status code: {logs_response.status_code}")
        time.sleep(interval)
