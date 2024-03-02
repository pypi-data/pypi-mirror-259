from commands.cancel_booking import cancel_booking
from commands.cancel_volunteer import cancel_volunteer
from commands.view_calendar import view_code_clinic_calendar
from commands.view_calendar import view_student_calendar
from commands.volunteer import volunteer_slot
from commands.booking import book_selected_slot
import utils


def cmd_invalid(option):
    print(f"No such option: '{option}'")
    print("Please select again")


def cmd_program_exit():
    print("Goodbye\n")
    exit(0)


def display_options():
    print("\nAvailable Commands\n")
    print(get_description())


def get_options():
    return {
        "1": {
            "option": "View Clinic Calendar",
            "description": "View current Code Clinic bookings",
            "function": view_code_clinic_calendar,
        },
        "2": {
            "option": "View Personal Calendar",
            "description": "View all current bookings",
            "function": view_student_calendar,
        },
        "3": {
            "option": "Book Assistance",
            "description": "Book a 30min Session",
            "function": book_selected_slot,
        },
        "4": {
            "option": "Volunteer Assistance",
            "description": "Volunteer 30min of assistance",
            "function": volunteer_slot,
        },
        "5": {
            "option": "Cancel Assistance Session",
            "description": "Cancel a booking",
            "function": cancel_booking,
        },
        "6": {
            "option": "Cancel Volunteer Session",
            "description": "Cancel a volunteering session",
            "function": cancel_volunteer,
        },
        "7": {
            "option": "Validate Connection",
            "description": "Ensure successful connection to Google Calendar",
            "function": utils.is_connected,
        },
        "8": {
            "option": "Configure",
            "description": "Provide/Update Programm Configurations",
            "function": utils.display_config,
        },
        "9": {
            "option": "Exit",
            "description": "Ends the Code Clinic bookings program",
            "function": cmd_program_exit,
        },
    }


def get_longest_length_of_options(options_dict):
    """
    Determine the length of the longest `option` value
    in provided dict

    Parameter
    ---------
    options_dict : dict[dict]
        mapping of UI input integer to function and
        its related UI descriptors

    Return
    ------
    int
        length of the option in provided dict
    """

    return max(len(cmd_descript["option"]) for cmd_descript in options_dict.values())


def get_description():
    """
    Provides a formatted string representation of
    available options

    Return
    ------
    str
        formatted string representation of available
        options
    """

    options_dict = get_options()
    longest = get_longest_length_of_options(options_dict)

    description = ""

    for index, cmd_descript in options_dict.items():
        cmd, descript, *_ = cmd_descript.values()
        description += f"   [{index}]  {cmd.ljust(longest)}\t\t{descript}\n\n"

    return description


def execute(option, creds, service, user_email):
    """
    Executor of executor pattern wherein user provided
    options is executed as per available commands

    Parameter
    ---------
    option : str::digit
        digit representing selection from UI

    creds : Credentials
        credentials to google api

    service : Resource
        resource request object to google api

    user_email : str
        user email extracted from `service`

    Return
    ------
    None
    """

    selection = get_options().get(option)

    if not selection:
        return cmd_invalid(option)

    func = selection.get("function")

    if option in "127":
        func(creds)
    elif option in "89":
        func()
    else:
        func(creds, service, user_email)

    print("\n" * 2)
