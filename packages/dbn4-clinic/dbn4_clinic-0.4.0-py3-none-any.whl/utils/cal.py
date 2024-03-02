from datetime import datetime, timedelta, date
import json
import os


import pytz


import utils


def code_clinic_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            file.write(json.dumps({}))


def code_student_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            file.write(json.dumps({}))


def create_day_event_pairs(events):
    """
    Provides an events dict where the keys
    are datetime.dateime objects created
    from str objects

    Parameter
    ---------
    events : dict[str, dict]
        str datetime to event pairs

    Return
    ------
    dict : dict[datetime, dict]
        datetime to event pairs of all
        events
    """

    return {datetime.fromisoformat(day): event for day, event in events.items()}


def display_menu_of_days(day_event_pairs):
    """
    Show user a formatted list of days as per
    provided `day_event_pairs`

    Parameter
    ---------
    day_event_pairs : dict[datetime, dict]

    Return
    ------
    None
    """

    days = sorted(day_event_pairs.keys())
    time_format = ": %H:%M%P"
    item_count = 4

    print("\n\n")

    for index, day in enumerate(days, start=1):
        print_formatted_day(index, day, time_format)

        if not divisible_by(index, item_count):
            print()

    print("\n\n")


def display_work_week(work_week):
    """Function display the working week with formatted dates."""
    week = work_week.copy()
    fifth_day = week.pop(4)
    num_of_days_left = len(week)

    print()

    for index in range(0, num_of_days_left, 2):
        utils.print_formatted_day(index + 1, week[index])
        utils.print_formatted_day(index + 2, week[index + 1])

    utils.print_formatted_day(5, fifth_day)
    print("\n\n")


def divisible_by(numerator, divisor):
    """
    Determine if `numerator` is divisible by `divisor`

    Parameters
    ----------
    numerator : int
        number being assessed

    divisor : int
        number being assessed against

    Return
    ------
    bool
        True if divisible else False
    """

    return bool(numerator % divisor)


def extract_work_week(week):
    """Function returns list of working days from the provided week"""
    work_week = []

    for day in week:
        if is_working_day(day):
            work_week.append(day)
    return work_week


def format_day(day, time_format=""):
    """
    Function validates a date to include the day of the
    month with the appropriate suffix, month abbreviation,
    and the day of the week.

    Parameters
    ----------
    day : datetime.day
        datetime.day object being formatted

    time_format: str
        format to be applied

    Return
    ------
    str
        formatted day in the form <DATE> <MONTH> <DAY> [TIME: optional]
    """

    ordinal = "st" if day.day in [1, 21, 31] else "th"
    return day.strftime(f"%d{ordinal} %b, %A{time_format}")


def format_time(start_time, end_time):
    """Function formats start time and end time in ISO format"""
    start_time_obj = datetime.fromisoformat(start_time)
    end_time_obj = datetime.fromisoformat(end_time)

    local_tz = pytz.timezone("Africa/Johannesburg")

    start_time_local = start_time_obj.astimezone(local_tz)
    end_time_local = end_time_obj.astimezone(local_tz)

    start_time_str = start_time_local.strftime("%Y-%m-%d %H:%M")
    end_time_str = end_time_local.strftime("%H:%M")

    return start_time_str, end_time_str


def get_current_week():
    """Function retrieves a list of dates representing the current week"""
    today = date.today()
    days_in_week = 7
    week = []

    for day in range(days_in_week):
        week.append(today + timedelta(days=day))
    return week


def get_date():
    """Function asks the user to select a date from the working week."""
    week = get_current_week()
    work_week = extract_work_week(week)

    display_work_week(work_week)
    num_of_days = len(work_week)
    selection = utils.make_user_selection(num_of_days, "day")
    return work_week[selection - 1]


def get_user_selection(events):
    """
    Have user select an event from a provided collection
    of events

    Parameter
    ---------
    events : dict[str, dict]
        str datetime to event pairs

    Return
    ------
    tuple : datetime, dict
        datetime to event pairs of selected event
    """

    day_event_pairs = create_day_event_pairs(events)
    display_menu_of_days(day_event_pairs)

    selection = make_user_selection(len(day_event_pairs), "day")
    return sorted(day_event_pairs.items())[selection - 1]


def is_booked(user_email, event):
    """
    Assess whether or not the provided event is
    booked

    Parameter
    ---------
    user_email : str
        email of user

    event : dict
        data relating to calendar event

    Return
    ------
    bool
        True if the event has someone other
        than the volunteer linked to it, else
        False
    """

    attendees = event.get("attendees", [])

    emails = [attendee for attendee in attendees]

    return bool(emails.count(user_email))


def is_creator(user_email, event):
    """
    Discern if proviced user email is that of
    the event creator

    Parameter
    ---------
    user_email : str
        user email extracted from `service`

    event : dict
        dict representation of event

    Return
    ------
    bool
        True if user email matches event
        creator else False
    """

    return bool(event.get("creator").count(user_email))


def is_working_day(day):
    """
    Check if the specified date is a working day (Monday to Friday).
    """
    return day.weekday() < 5


def make_user_selection(max_num, option):
    """
    Function asks the user to select a day from the
    provided working week

    Parameter
    ---------
    max_num : int
        highest number user is allowed to enter

    Return
    ------
    int
        positive number representing user's selection
        from the provided work week
    """

    while True:
        range_ = "[1]" if max_num == 1 else f"[1-{max_num}]"
        message = f"Please selected a {option} {range_}:\t\t\t\t"

        selection = input(message)

        if not selection.isdigit():
            continue

        selection_int = int(selection)

        if 1 <= selection_int <= max_num:
            return selection_int


def print_formatted_day(index, day, time_format=""):
    """
    Function outputs a formatted representation of a day.

    Parameters
    ----------
    index : int
        provided index number used when printing list

    day : datetime.day
        datetime.day object being formatted

    time_format: str
        format to be applied

    Return
    ------
    None
    """

    formatted_day = format_day(day, time_format)

    index_str = str(index) if index >= 10 else f"0{index}"

    print(f"   [{index_str}]  {formatted_day}\t\t", end="")


def read_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def update_local_db(events, deleted_day):
    """
    Save changes to calendar onto local database

    Parameter
    ---------
    events : dict[str, dict]
        events as read in from the local db

    deleted_day : datetime.datetime
        datetime object representing the day
        that had been deleted

    Return
    ------
    None
    """

    day_isoformat = deleted_day.isoformat()

    events_updated = {
        day: event for day, event in events.items() if not day.count(day_isoformat)
    }

    write_into_file(utils.CALENDAR_DATA, events_updated)


def write_into_file(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file)
