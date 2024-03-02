"""
Authentication module for project, ensures that the user's
credentials and token exit and have been validated. In
cases where there are no credentials, please see the REAME.

Where no token is present, a new one is created, assuming
that the credentials are authentic.
"""

import pathlib
import sys
import os


from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import requests


sys.path.append(pathlib.Path.cwd().as_posix())


from utils import config


def authenticate():
    """
    Athenticate user credentials assuming credentials file
    provided. For details please refer to README

    Parameters
    ----------
    creds : Credentials
        credentials to google api

    token_path : str
        posix file path to token

    Return
    ------
    Credentials
        the constructed credentials
    """

    config.create_working_directories()

    credentials_path = config.FILENAMES["credentials"]
    token_path = config.FILENAMES["token"]

    if not is_creds_file(credentials_path):
        raise FileNotFoundError("Credentials not found. Please see `README.md`")

    creds = (
        load_creds_from_file(token_path, config.SCOPES)
        if is_token_file(token_path)
        else None
    )

    if not is_creds_valid(creds):
        creds = re_authenticate(creds, token_path, credentials_path, config.SCOPES)
        save_re_authecation(creds, token_path)

    return creds


def build_service(creds):
    """
    Builds a Google Calendar API Service around which
    all the program functionality is to be based

    Parameters
    ----------
    creds : Credentials
        credentials to google api

    Return
    ------
    service
        a googleapiclient discovery Resource
    """

    return build("calendar", "v3", credentials=creds)


def get_user_email(service):
    """
    Call Google Calendar API Service, requesiting the
    email of the current user

    Parameters
    ----------
    service : Resource
        resource request object to google api

    Return
    ------
    str
        email of current user
    """

    primary = service.calendars().get(calendarId="primary")
    return primary.execute().get("summary")


def initialise():
    """
    Ensure that the program is initialised for usage,
    included being the user's credentials placed in
    the required directory

    For details please refer to README

    Return
    ------
    None
    """

    config.create_working_directories()
    credentials = config.DIR_CREDENTIALS.joinpath("credentials.json")
    token = config.DIR_CREDENTIALS.joinpath("token.json")

    if token.is_file():
        return config.display_config()
    elif not credentials.is_file():
        print(
            "Let's get you set up. For ease of use, please follow along with the README"
        )
        while not credentials.is_file():
            ...

    print("and here we go ^_^")

    if pathlib.Path.exists(config.FILENAMES["credentials"]):
        config.display_config()


def is_connected(creds):
    """
    Ensures that the session is connected to googleapis
    althewhile having valid credentials

    Parameters
    ----------
    creds : Credentials
        credentials to google api

    Return
    ------
    bool
        True if connected else False
    """

    base = f"https://www.googleapis.com/oauth2/v3/tokeninfo?access_token="
    url = f"{base}{creds.token}"

    try:
        return requests.get(url).ok
    except Exception:
        print(";( hmmm ... seems we can't talk to the calendars")
        return False


def is_creds_file(credentials_path):
    """
    Determine if provided posix file path
    to credentials file is valid

    Parameters
    ----------
    credentials_path : str
        posix file path to credentials

    Return
    ------
    bool
        True if file exists else False
    """

    return os.path.exists(credentials_path)


def is_stale_creds(creds):
    """
    Determine if provided credentials need
    be refreshed

    Parameters
    ----------
    credentials_path : str
        posix file path to credentials

    Return
    ------
    bool
        True if file exists else False
    """

    return creds and creds.expired and creds.refresh_token


def is_creds_valid(creds):
    """
    Validate provided credentials

    Parameters
    ----------
    creds : Credentials
        credentials to google api

    Return
    ------
    bool
        True if credentials valid else
        False
    """

    return creds and creds.valid


def is_token_file(token_path):
    """
    Determine if provided posix file path
    to token file is valid

    Parameters
    ----------
    token_path : str
        posix file path to token

    Return
    ------
    bool
        True if file exists else False
    """

    return os.path.exists(token_path)


def load_creds_from_file(token_path, scopes):
    """
    Provides credentials as loaded and parsed from
    provided token

    Parameters
    ----------
    token_path : str
        posix file path to token

    scopes : list[str]
        list of calendar scopes for which the
        pointed to token is valid

    Return
    ------
    Credentials
        the constructed credentials
    """

    return Credentials.from_authorized_user_file(
        filename=token_path,
        scopes=scopes,
    )


def re_authenticate(creds, token_path, credentials_path, scopes):
    """
    Re-Authenticate provided credentials

    Parameters
    ----------
    creds : Credentials
        credentials to google api

    token_path : str
        posix file path to token

    credentials_path : str
        posix file path to credentials

    scopes : list[str]
        list of calendar scopes for which
        the pointed to token is valid

    Return
    ------
    Credentials
        the constructed credentials
    """

    if is_stale_creds(creds):
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secrets_file=credentials_path,
            scopes=scopes,
        )
        creds = flow.run_local_server(port=0)
    return creds


def save_re_authecation(creds, token_path):
    """
    Save re-athenticated credentials for file

    Parameters
    ----------
    creds : Credentials
        credentials to google api

    token_path : str
        posix file path to token

    Return
    ------
    Credentials
        the constructed credentials
    """

    with open(token_path, "w") as token:
        token.write(creds.to_json())


def tell_user_no_connection():
    """Inform user when no internet connection is available"""

    print("Cancellation can't be made at this time:")
    print("\tplease retry at a later time")
