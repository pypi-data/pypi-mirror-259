import datetime as dt
import os.path
import pathlib
import sys


sys.path.append(pathlib.Path.cwd().as_posix())

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from prettytable import PrettyTable


from utils import auth
from utils import config
from utils import cal


credentials_filename = config.FILENAMES["credentials"]
token_filename = config.FILENAMES["token"]


file_path = os.path.expanduser("~")
student_calendar = os.path.join(file_path, "student_calendar.json")


def filter_data(stored_data):
    """Filters out past events from stored_data based on current date and time.
    Parameters:
    - stored_data (dict): A dictionary containing event start times as keys and event details as values.
    Returns:
    - dict: A dictionary containing only future events."""
    current_datetime = dt.datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()

    return {
        start: event_data
        for start, event_data in stored_data.items()
        if dt.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z").date() > current_date
        or (
            dt.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z").date() == current_date
            and dt.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z").time() > current_time
        )
    }


def get_code_clinic_calendar_events(creds):
    """Retrieves the events from the Google Calendar for the next 7 days.
    Parameters:
    - creds: Google API credentials.
    Returns:
    - list: A list of events.r"""
    try:
        service = build("calendar", "v3", credentials=creds)
        now = dt.datetime.utcnow().isoformat() + "Z"
        next_days = (dt.datetime.utcnow() + dt.timedelta(days=7)).isoformat() + "Z"
        event_request = (
            service.events()
            .list(
                calendarId=config.CALENDAR_ID,
                timeMin=now,
                timeMax=next_days,
                maxResults=20,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = event_request.get("items", [])

    except HttpError as error:
        print("An error occurred:", error)
    return events


def update_calendar_data(events, calendar_data):
    """Saves the events to the local calendar data file.
    Parameters:
    - events (list): A list of event dictionaries from Google Calendar API.
    - calendar_data (str): Path to the local JSON file where calendar data is stored.
    """
    stored_data = cal.read_from_file(calendar_data)
    lastest_data = filter_data(stored_data)

    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))
        summary = event["summary"]
        event_ID = event["id"]
        creator = event.get("creator", {}).get("email", "")
        attendees = event.get("attendees", [])
        campus = event.get("location", "")
        description = event.get("description", "")
        attendee_emails = [
            attendee["email"] for attendee in attendees if "email" in attendee
        ]

        lastest_data[start] = {
            "summary": summary,
            "creator": creator,
            "attendees": attendee_emails,
            "location": campus,
            "description": description,
            "end": end,
            "id": event_ID,
        }
    cal.write_into_file(calendar_data, lastest_data)


def is_update_needed(calendar_data_file):
    """Checks if an update is needed for the local calendar
    data based on the presence of events for the next 7 days.
    Parameters:
    - calendar_data_file (str): Path to the local JSON file containing calendar data.
    Returns:
    - bool: True if an update is needed, otherwise False."""
    stored_data = cal.read_from_file(calendar_data_file)

    if stored_data == {}:
        return True

    today = dt.datetime.now().date()
    seven_days_from_now = today + dt.timedelta(days=7)
    stored_event_dates = [
        dt.datetime.strptime(event.split("T")[0], "%Y-%m-%d").date()
        for event in stored_data.keys()
    ]
    for single_date in (today + dt.timedelta(n) for n in range(7)):
        if single_date not in stored_event_dates and single_date <= seven_days_from_now:
            return True
    return False


def print_code_clinic_calendar(calendar_data):
    """
    Prints a table of upcoming code clinic events.
    Reads the specified code clinic calendar data file, filters events based on the current date and time,
    and presents the information in a well-formatted table that includes details like topic, date, start and end times,
    location, volunteer name, event ID, and the event's booking status.
    """
    stored_data = cal.read_from_file(calendar_data)

    current_datetime = dt.datetime.now()
    current_time = current_datetime.now().time()
    current_date = current_datetime.date()

    events_output = PrettyTable()
    events_output.field_names = (
        "Topic",
        "Date",
        "Start Time",
        "End Time",
        "Campus",
        "Vounteer",
        "Status",
    )

    if not stored_data:
        print("No upcoming events found")
        return

    print("Upcoming events.\n")

    for start, event_data in stored_data.items():
        event_datetime = dt.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S%z")
        if event_datetime.date() > current_date or (
            event_datetime.date() == current_date
            and event_datetime.time() > current_time
        ):

            if "T" in start:
                date, start_time = start.split("T")
            else:
                date = start
                start_time = ""
            end = event_data["end"]
            if "T" in end:
                _, end_time = end.split("T")
            else:
                end_time = ""
            summary = event_data.get("summary")
            creator = event_data["creator"]
            attendee = event_data.get("attendees")
            campus = event_data.get("location")
            status = "Booked" if attendee != [] else "Available"

            events_output.add_row(
                [
                    summary,
                    date,
                    start_time[0:5],
                    end_time[0:5],
                    campus,
                    creator,
                    status,
                ]
            )

    print(events_output)


def get_student_calendar_events(creds):
    """Retrieves the upcoming events from the student's Google Calendar.
    This function makes a request to the Google Calendar API to fetch the next 7 upcoming events from the primary calendar.
    It handles exceptions by printing an error message if the request fails.
    Returns:
        list: A list of upcoming events, each represented as a dictionary."""
    try:
        service = build("calendar", "v3", credentials=creds)
        now = dt.datetime.now().isoformat() + "Z"

        event_request = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=20,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = event_request.get("items", [])

    except HttpError as error:
        print("An error occurred:", error)
    return events


def update_student_calendar(events):
    """Updates the local JSON file with new events from the student's Google Calendar.
    This function reads the current events from a local JSON file, filters out past events,
    and updates it with new events fetched from the Google Calendar.
    Each event's start and end times, summary, ID, creator, attendee, and a description are stored.
    """
    student_data = cal.read_from_file(student_calendar)

    day = dt.datetime.now().date()

    student_data = {
        start: event_data
        for start, event_data in student_data.items()
        if dt.datetime.strptime(start.split("T")[0], "%Y-%m-%d").date() >= day
    }

    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))
        summary = event["summary"]
        event_ID = event["id"]
        creator = event.get("creator", {}).get("email", "")
        attendee = event.get("attendees", [])
        description = event.get("description", "No description provided")
        student_data[start] = {
            "summary": summary,
            "creator": creator,
            "attendees": attendee,
            "description": description,
            "end": end,
            "id": event_ID,
        }
    cal.write_into_file(student_calendar, student_data)


def is_student_update_needed(student_calendar):
    """Determines whether the student calendar needs to be updated with new events.
    By reading the existing events from the student calendar file, this function checks if there are any events within the next 7 days
    that are not already stored. If there are missing events, it indicates that an update is needed.
    """
    student_data = cal.read_from_file(student_calendar)

    if student_data == {}:
        return True
    today = dt.datetime.now().date()
    seven_days_from_now = today + dt.timedelta(days=7)
    stored_event_dates = [
        dt.datetime.strptime(event.split("T")[0], "%Y-%m-%d").date()
        for event in student_data.keys()
    ]
    for single_date in (today + dt.timedelta(n) for n in range(7)):
        if single_date not in stored_event_dates and single_date <= seven_days_from_now:
            return True
    return False


def print_student_calendar():
    """Prints a table of upcoming events from the student's calendar.
    Reads the student calendar data file and displays the upcoming events for
    the next 7 days in a table format, including
    the date, start time, end time, and description of each event."""
    student_data = cal.read_from_file(student_calendar)
    events_output = PrettyTable()

    events_output.field_names = (
        "Date",
        "Start Time",
        "End Time",
        "Description",
    )

    if not student_data:
        print("No upcoming events found")
        return

    print("Upcoming events.\n")

    today = dt.datetime.now().date()
    for start, event_data in student_data.items():
        event_date = dt.datetime.strptime(start.split("T")[0], "%Y-%m-%d").date()
        if today <= event_date <= (today + dt.timedelta(days=7)):
            if "T" in start:
                date, start_time = start.split("T")
            else:
                date = start
                start_time = ""
            end = event_data["end"]
            if "T" in end:
                _, end_time = end.split("T")
            else:
                end_time = ""
            summary = event_data["summary"]
            events_output.add_row([date, start_time[0:5], end_time[0:5], summary])

    print(events_output)


def view_student_calendar(creds):
    """This function ensures the student calendar file is prepared,
    fetches the latest events from Google Calendar,
    checks if an update is needed, updates the local student calendar data
    file with new events, and finally prints the updated events."""
    cal.code_student_file(student_calendar)
    events = get_student_calendar_events(creds)
    is_student_update_needed(student_calendar)
    update_student_calendar(events)
    print_student_calendar()


def view_code_clinic_calendar(creds):
    """this function ensures the code clinic calendar file is prepared, fetches
    the latest events from Google Calendar, checks if an update is needed,
    updates the local code clinic calendar data file
    with new events, and prints the updated events.
    """
    calendar_data = config.FILENAMES["calendar_data"]
    cal.code_clinic_file(calendar_data)
    events = get_code_clinic_calendar_events(creds)
    is_update_needed(calendar_data)
    update_calendar_data(events, calendar_data)
    print_code_clinic_calendar(calendar_data)


def init(creds):
    """Get all the calendars on the first run"""
    cal.code_student_file(student_calendar)

    student_events = get_student_calendar_events(creds)
    is_student_update_needed(student_calendar)
    update_student_calendar(student_events)

    calendar_data = config.FILENAMES["calendar_data"]

    cal.code_clinic_file(calendar_data)
    clinic_events = get_code_clinic_calendar_events(creds)
    is_update_needed(calendar_data)
    update_calendar_data(clinic_events, calendar_data)


if __name__ == "__main__":

    config.create_working_directories()
    creds = auth.authenticate()

    calendar_type = input(
        "What calendar do you want to view student or code clinic: "
    ).lower()

    if calendar_type == "student":
        view_student_calendar(creds)

    elif calendar_type == "code clinic":
        view_code_clinic_calendar(creds)
    else:
        print("incorrect calendar chosen")
