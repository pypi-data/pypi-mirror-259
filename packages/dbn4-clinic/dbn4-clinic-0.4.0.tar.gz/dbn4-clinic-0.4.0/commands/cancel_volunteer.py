import pathlib
import sys


sys.path.append(pathlib.Path.cwd().as_posix())


from googleapiclient.errors import HttpError


import utils


def parse_events(user_email):
    """
    isoformat datetime to event pairs of events volunteered
    to by user, with no booking attached

    Return
    ------
    tuple[dict]
        tuple of two isoformat datetime-event pair
        dicts with all events and user deletable events
    """

    events = utils.read_from_file(utils.CALENDAR_DATA)
    deletable = {
        day: event
        for day, event in events.items()
        if utils.is_creator(user_email, event)
        and not utils.is_booked(user_email, event)
    }

    return events, deletable


def cancel_volunteer(creds, service, user_email):
    """
    Cancels a volunteer's slot from the Google Calendar

    Parameter
    ---------
    creds : Credentials
        credentials to google api

    service : Resource
        resource request object to google api

    user_email : str
        user email extracted from `service`

    Return
    ------
    bool
        True if the event has be cancelled
        else False
    """

    events, deletable = parse_events(user_email)

    if not deletable:
        print("There look to be no events at present")
        return False

    print("\nSelect day for cancelling volunteering")

    day, event = utils.get_user_selection(deletable)

    event_id = event.get("id")
    is_deleted = delete_event(service, event_id)

    if not is_deleted:
        return is_deleted

    utils.update_local_db(events, day)
    print("\nAnd all is done ;)")
    return is_deleted


def delete_event(service, provided_event_id):
    """
    Api Call to delete the proved event id, assumption
    being made that the id has been validated

    Parameter
    ---------
    service : Resource
        resource request object to google api

    provided_id : str
        user provided event id under evaluation

    Return
    ------
    bool
        True if the event has be deleted
        else False
    """

    deleter = service.events().delete(
        calendarId=utils.CALENDAR_ID,
        eventId=provided_event_id,
    )

    try:
        return deleter.execute() == ""
    except HttpError as error:
        message = error.error_details.pop().get("message")
        print(f"Hmmm ... according to our friends at Google, '{message}'")
        print("Please consider double checking for us ^_^")

    return False


if __name__ == "__main__":
    creds = utils.authenticate()
    service = utils.build_service(creds)
    email = utils.get_user_email(service)

    cancel_volunteer(creds, service, email)
