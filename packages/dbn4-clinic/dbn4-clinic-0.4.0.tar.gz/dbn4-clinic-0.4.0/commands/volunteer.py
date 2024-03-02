from datetime import datetime, timedelta
import pathlib
import sys


sys.path.append(pathlib.Path.cwd().as_posix())


from googleapiclient.errors import HttpError
import pytz


import utils


def create_event(service, start_time, end_time, topic, email, campus):
    """Function creates events for volunteer using service, start time, end time,
    topic, email"""
    event = {
        "summary": topic,
        "start": {"dateTime": start_time, "timeZone": "Africa/Johannesburg"},
        "end": {"dateTime": end_time, "timeZone": "Africa/Johannesburg"},
        "creator": [{"email": email}],
        "campus": campus,
    }

    try:
        service.events().insert(calendarId=utils.CALENDAR_ID, body=event).execute()
        start_time_str, end_time_str = utils.format_time(start_time, end_time)
        print(f"Booked slot on {start_time_str} to {end_time_str}")

    except HttpError as error:
        print(f"An error occurred: {error}")


def store_event_data(event):
    """Function saves events to json file"""
    stored_data = utils.read_from_file(utils.CALENDAR_DATA)

    start_time = event["start"]["dateTime"]
    stored_data[start_time] = {
        "id": event["id"],
        "summary": event["summary"],
        "creator": event.get("creator", {}).get("email", ""),
        "attendees": [attendee["email"] for attendee in event.get("attendees", [])],
        "end": event["end"]["dateTime"],
        "campus": event.get("location", ""),
    }

    utils.write_into_file(utils.CALENDAR_DATA, stored_data)


def is_volunteer_slot_available(creds, service, start_time, end_time):
    """
    Function checks if a slot on the specified calendar is available..
    """

    events_result = (
        service.events()
        .list(
            calendarId=utils.CALENDAR_ID,
            timeMin=start_time,
            timeMax=end_time,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])
    return not bool(events)


def volunteer_slot(creds, service, email):
    """Function checks if volunteer slot is still available to book slot
    It uses date and time object to check slot
    Validate  past dates
    """

    selected_date, time, topic, campus = get_inputs()

    now = datetime.utcnow()
    time = datetime.strptime(time, "%H:%M")

    start_time_obj = datetime.combine(selected_date, time.time())

    johannesburg_tz = pytz.timezone("Africa/Johannesburg")
    start_time_obj = johannesburg_tz.localize(start_time_obj)
    end_time_obj = start_time_obj + timedelta(minutes=30)
    now = datetime.now(pytz.UTC)

    if start_time_obj < now:
        print("\nCannot book a past date.")
        return

    if not (8 <= start_time_obj.hour < 16):
        print("Booking can only be made between 08:00 and 16:00.")
        return

    start_time_formatted = start_time_obj.isoformat()
    end_time_formatted = end_time_obj.isoformat()

    if is_volunteer_slot_available(
        creds, service, start_time_formatted, end_time_formatted
    ):
        create_event(
            service, start_time_formatted, end_time_formatted, topic, email, campus
        )
    else:
        print("This slot is already booked.")


def format_day(day):
    """Function validates a date to include the day of the month with the appropriate suffix,
    month abbreviation, and the day of the week."""
    f = "st" if day.day in [1, 21, 31] else "th"
    return day.strftime(f"%d{f} %b, %A")


def print_formatted_day(index, day):
    """Function outputs a formatted representation of a day."""
    formatted_day = format_day(day)
    print(f"   [{index}]  {formatted_day}\t\t", end="")


def display_campuses(campuses_list):
    print("\n")

    for i, campus in enumerate(campuses_list, start=1):
        print(f"   [{i}]  {campus}\t\t", end="")

    print("\n\n")


def get_campuses():
    campuses_list = ["DBN", "JBH", "CPT"]

    display_campuses(campuses_list)
    num_of_campuses = len(campuses_list)
    selection = utils.make_user_selection(num_of_campuses, "campus")
    return campuses_list[selection - 1]


def get_time():
    """Function asksthe user to enter the time for the slot (24-hour format)."""
    while True:
        time = input("\nEnter the time for the slot (24-hour format):\t\t")

        if utils.validate_time(time):
            return time


def get_inputs():
    """Function retrieves user inputs for date, time, and topic."""
    print("\nSelect day for volunteering\n")
    selected_date = utils.get_date()
    time = get_time()
    topic = input("\nEnter the topic for the booking:\t\t\t")
    campus = get_campuses()
    return selected_date, time, topic, campus


if __name__ == "__main__":
    creds = utils.authenticate()
    service = utils.build_service(creds)
    email = utils.get_user_email(service)

    volunteer_slot(creds, service, email)
