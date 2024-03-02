from utils.auth import authenticate
from utils.auth import build_service
from utils.auth import initialise
from utils.auth import is_connected
from utils.auth import get_user_email
from utils.auth import tell_user_no_connection
from utils.cal import code_clinic_file
from utils.cal import code_student_file
from utils.cal import is_booked
from utils.cal import is_creator
from utils.cal import format_time
from utils.cal import get_date
from utils.cal import get_user_selection
from utils.cal import make_user_selection
from utils.cal import print_formatted_day
from utils.cal import read_from_file
from utils.cal import update_local_db
from utils.cal import write_into_file
from utils.check_input_error import validate_email
from utils.check_input_error import validate_time
from utils.config import CALENDAR_ID
from utils.config import FILENAMES
from utils.config import SCOPES
from utils.config import clear_screen
from utils.config import create_working_directories
from utils.config import display_config


CALENDAR_DATA = FILENAMES.get("calendar_data")
CREDENTIALS = FILENAMES.get("credentials")
TOKEN = FILENAMES.get("token")
