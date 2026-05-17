# auth_youtube.py
from pathlib import Path
import httplib2

from oauth2client.file import Storage
from oauth2client.tools import run_flow, argparser
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.discovery import build

BASE_DIR = Path(__file__).parent

CLIENT_SECRETS_FILE = str(BASE_DIR / "client_secret.json")

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtubepartner",
]

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

oauth_store = BASE_DIR / "youtube-oauth2.json"


def authenticate():
    flow = flow_from_clientsecrets(
        CLIENT_SECRETS_FILE,
        scope=SCOPES,
    )

    storage = Storage(str(oauth_store))
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        flags = argparser.parse_args(args=[])
        flags.noauth_local_webserver = True
        credentials = run_flow(flow, storage, flags)

    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        http=credentials.authorize(httplib2.Http()),
    )

    print("Authenticated!")
    print("Saved token to:", oauth_store)


if __name__ == "__main__":
    authenticate()