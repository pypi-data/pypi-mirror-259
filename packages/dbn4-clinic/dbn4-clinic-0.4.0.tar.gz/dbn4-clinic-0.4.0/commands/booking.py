from datetime import datetime
import pathlib
import sys


sys.path.append(pathlib.Path.cwd().as_posix())


from googleapiclient.errors import HttpError

import utils


calendar_data = utils.FILENAMES["calendar_data"]


def get_event_id(service):
    """
    Display available time slots for booking from the calendar.

    This function fetches the current week's work schedule, allows the user to select a date,
    and then displays available time slots on that date for booking.

    Parameters:
    - service: Authorized Google Calendar service instance.

    Returns:
    - The event ID of the slot.
    """

    print("\nSelect day for booking\n")
    selected_date = utils.get_date()
    time_slots = get_available_time_slots(service, selected_date)

    print("\nAvailable Events:\n\n")
    if not time_slots:
        return None

    for index, slot in enumerate(time_slots, start=1):
        start_time_str, end_time_str = utils.format_time(slot["start"], slot["end"])
        date_str = f"[{index}] Date: {start_time_str}"
        time_str = f"Time: {start_time_str} to {end_time_str}"
        campus_str = f"Campus: {slot.get('location')}"
        topic_str = f"Topic: {slot.get('summary')}"
        print(f"   {date_str}\t\t{time_str}\t\t{campus_str}\t\t{topic_str}")
    print("\n")
    slot_index = utils.make_user_selection(len(time_slots), "day")
    return time_slots[slot_index - 1]["event_id"]


def get_available_time_slots(service, selected_date):
    """
    Fetch available time slots for a selected date.

    This function queries the Google Calendar API for events on a given date,
    filters out slots without attendees as available, and returns these slots.

    Parameters:
    - service: Authorized Google Calendar service instance.
    - selected_date: The date for which to find available time slots (datetime.date object).

    Returns:
    - A list of available time slots (each as a dictionary containing start time, end time, and event ID).
    """

    selected_date_str = selected_date.isoformat()
    start_time = datetime.fromisoformat(f"{selected_date_str}T00:00:00Z")
    end_time = datetime.fromisoformat(f"{selected_date_str}T23:59:59Z")

    events_result = (
        service.events()
        .list(
            calendarId=utils.CALENDAR_ID,
            timeMin=start_time.isoformat(),
            timeMax=end_time.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = events_result.get("items", [])
    available_slots = []

    for event in events:
        if not event.get("attendees"):
            slots = {
                "start": event["start"]["dateTime"],
                "end": event["end"]["dateTime"],
                "event_id": event["id"],
                "summary": event.get("summary"),
                "campus": event.get("location"),
            }
            available_slots.append(slots)

    return available_slots


def book_selected_slot(creds, service, email):
    """
    Book a selected slot for the user by adding them as an attendee to the event.

    Parameters:
    - service: Authorized Google Calendar service instance.
    - email: Email address of the user to be added as an attendee.
    - creds: Credentials for calendar .

    If the event already has attendees, it checks if the user is not already registered
    before adding them. It updates the event with the new attendee list.

    Returns:
    - None
    """

    stored_data = utils.read_from_file(utils.CALENDAR_DATA)
    event_id = get_event_id(service)

    if not event_id:
        print("\nNo events avaliable")
        return

    try:
        event = (
            service.events()
            .get(calendarId=utils.CALENDAR_ID, eventId=event_id)
            .execute()
        )

        creator_email = event.get("creator", {}).get("email", "")
        if creator_email == email:
            print("\nYou cannot book your own event.")
            return

        if "attendees" in event:
            if any(attendee["email"] == email for attendee in event["attendees"]):
                print("\nYou are already registered for this event.")
                return
            event["attendees"].append({"email": email})
        else:
            event["attendees"] = [{"email": email}]

        updated_event = (
            service.events()
            .update(calendarId=utils.CALENDAR_ID, eventId=event_id, body=event)
            .execute()
        )
        print(f"\nSuccessfully booked: {updated_event.get('summary')}")

    except Exception as e:
        print(f"An error occurred: {e}")

    utils.write_into_file(utils.CALENDAR_DATA, stored_data)


def get_event_details(service, event_id):
    """
    Fetch the details of an event by its ID.

    Parameters:
    - service: Authorized Google Calendar service instance.
    - event_id: The ID of the event to retrieve details for.

    Returns:
    - The event details as a dictionary if successful, None otherwise.
    """

    try:
        event = (
            service.events()
            .get(calendarId=utils.CALENDAR_ID, eventId=event_id)
            .execute()
        )
        return event
    except HttpError as error:
        print(f"\nAn error occurred: {error}")
        return None


if __name__ == "__main__":
    creds = utils.authenticate()
    service = utils.build_service(creds)
    student_email = utils.get_user_email(service)
    book_selected_slot(creds, service, student_email)
