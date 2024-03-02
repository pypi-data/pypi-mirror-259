import pathlib
import sys


sys.path.append(pathlib.Path.cwd().as_posix())


from googleapiclient.errors import HttpError


import utils


def extract_removeable_events(student_email, events):
    """check in the events if there are any events to cancel"""
    removeable = {}

    for day, event in events.items():
        attendees = event.get("attendees")
        creator = event.get("creator")

        if (
            attendees is not None
            and student_email in attendees
            and creator
            and not utils.is_creator(student_email, event)
        ):
            removeable[day] = event

    return removeable


def cancel_attendee(service, event_id, body):
    """cancels the user as the attendee to a event"""
    updater = service.events().update(
        calendarId=utils.CALENDAR_ID, eventId=event_id, body=body
    )
    try:
        updater.execute()
        return True
    except HttpError as error:
        message = error.error_details.pop().get("message")
        print(f"Error: {message}")
    return False


def cancel_booking(creds, service, student_email):
    """
     Removes the specified attendee from an event.

    Args:
        service: Google Calendar service object.
        # event_ID (str): Event ID to modify.
        student_email (str): Email of the attendee to remove.
    """

    events = utils.read_from_file(utils.CALENDAR_DATA)

    removeable_events = extract_removeable_events(student_email, events)

    if events.items() is None or removeable_events == {}:
        print("You have no booking sessions to cancel.")
        return

    print("Please select booking session you want to cancel")

    day, event_body = utils.get_user_selection(removeable_events)

    event_id = event_body.get("id")
    event = (
        service.events().get(calendarId=utils.CALENDAR_ID, eventId=event_id).execute()
    )

    attendees = event["attendees"]
    updated_attendees = [
        attendee for attendee in attendees if attendee != student_email
    ]

    if len(updated_attendees) < len(attendees):
        event["attendees"] = updated_attendees

    is_cancelled = cancel_attendee(service, event_id, event)

    if not is_cancelled:
        return is_cancelled

    utils.update_local_db(events, day)
    print(f"\nRemoved {student_email} from the event successfully.")
    return is_cancelled


if __name__ == "__main__":
    creds = utils.authenticate()
    service = utils.build_service(creds)
    student_email = utils.get_user_email(service)

    cancel_booking(creds, service, student_email)
