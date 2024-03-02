"""
Provide functionality for creating hidden directories for user data as well as
asserting a working connection to www.googleapis.com servers
"""

from datetime import datetime
import pathlib
import json
import os


CALENDAR_ID = "c_9134fa9f242bd5456b54432c0c2a72e0b55713fc548634cfde408ce6da2fd584@group.calendar.google.com"
SCOPES = ["https://www.googleapis.com/auth/calendar"]


DIR_CODE_CLINIC = pathlib.Path.home().joinpath(".code_clinic")
DIR_CALENDAR_DATA = DIR_CODE_CLINIC.joinpath("calendar_data")
DIR_CREDENTIALS = DIR_CODE_CLINIC.joinpath("credentials")


FILENAMES = {
    "calendar_data": DIR_CALENDAR_DATA.joinpath("calendar_data.json").as_posix(),
    "credentials": DIR_CREDENTIALS.joinpath("credentials.json").as_posix(),
    "token": DIR_CREDENTIALS.joinpath("token.json").as_posix(),
}


def clear_screen():
    """
    Removes content from the terminal

    Return
    ------
    None
    """

    os.system("cls||clear")
    print("\n" * 4)


def create_working_directories():
    """
    Creation of working directories should they not already
    exist. Should there be any files or directories, the
    data is left untouched

    Return
    ------
    None
    """

    if not pathlib.Path.exists(DIR_CODE_CLINIC):
        DIR_CODE_CLINIC.mkdir(exist_ok=True)
        DIR_CREDENTIALS.mkdir(exist_ok=True)
        DIR_CALENDAR_DATA.mkdir(exist_ok=True)


def display_config():
    """
    Displays user configuration details

    Return
    ------
    None
    """

    creds_path = FILENAMES.get("credentials")
    str_expiry = get_token_expiry_date()

    if not str_expiry:
        print("Credentials invalid, please refet to README")
        return

    date_obj = datetime.strptime(str_expiry, "%Y-%m-%dT%H:%M:%S.%fZ")
    expiry = date_obj.strftime("%B %d, %Y")

    print(
        "Config {\n"
        + f"\tcreds_path: '{creds_path},'\n"
        + f"\texpiry_date: {expiry},\n"
        + "}"
    )


def get_token_expiry_date():
    """
    Extract expiration date of the current token as
    generated from the provided user credentials

    Return
    ------
    None
    """

    try:
        with open(FILENAMES.get("token")) as token:
            return json.load(token).get("expiry")
    except FileNotFoundError:
        ...
