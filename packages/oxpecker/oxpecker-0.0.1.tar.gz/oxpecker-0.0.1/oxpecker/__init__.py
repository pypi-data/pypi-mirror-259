"""Basic setup for oxpecker package."""

import logging
import os
from pathlib import Path
import shutil

import requests

try:
    API_URL = f'https://{os.environ["OXPECKER_HOST"]}:{os.environ["OXPECKER_PORT"]}/oxpecker/api/v1/'
    WS_URL = f'wss://{os.environ["OXPECKER_HOST"]}:{os.environ["OXPECKER_PORT"]}/oxpecker-client-connect'
except KeyError:
    logging.warning(
        "OXPECKER_HOST or OXPECKER_PORT environment variable is not set; many commands would not work."
    )
    API_URL = ""
    WS_URL = ""

API_ENDPOINTS = {
    "login": "auth/login",
    "upload": "files/upload",
    "task_create": "tasks",
    "task_list": "tasks/search",
    "file_check": "files/check-exist",
    "task_inspect": "tasks",
}

LANGUAGES = [
    "c",
    "cpp",
    "csharp",
    "go",
    "java",
    "kotlin",
    "javascript",
    "typescript",
    "python",
    "ruby",
    "swift",
]

WORK_DIR = Path("~/.oxpecker").expanduser()
WORK_DIR.mkdir(parents=True, exist_ok=True)

if not (CODEQL_EXE := shutil.which("codeql")):
    logging.warning("`codeql` is not found; many commands would not work.")

try:
    auth = {"Authorization": (token := os.environ.get("OXPECKER_TOKEN"))}
    if not token:
        with open(WORK_DIR / "token", encoding="utf-8") as tf:
            auth = {"Authorization": tf.read()}
except (OSError, FileNotFoundError):
    logging.warning(
        "Oxpecker token not found; many commands would not work.\n"
        "Use `oxpecker login` to get the token.\n"
    )
    auth = {"Authorization": "INVALID TOKEN"}

session = requests.Session()
session.headers.update(auth)
