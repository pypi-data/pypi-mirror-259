"""
Test the configuration module of the module
"""

from unittest.mock import patch
from unittest import TestCase
from unittest import main
from unittest import skip
import pathlib
import sys
import os


sys.path.append(pathlib.Path.cwd().as_posix())


from utils import config


@skip
class TestConfig(TestCase):

    @staticmethod
    def get_output(mock_print):
        """Provide mocked print out as a lowercased string"""

        calls = mock_print.call_args_list
        return " ".join(str(call_.args) for call_ in calls).lower()

    def test_calendar_id(self):
        """
        Assert that the used calendar id is linked to google
        calendar
        """

        self.assertTrue("calendar" in config.CALENDAR_ID.lower())
        self.assertTrue("google" in config.CALENDAR_ID.lower())

    def test_scopes(self):
        """Assert that the used scope is for the google calendar"""

        scopes = ", ".join(scope.lower() for scope in config.SCOPES)
        self.assertTrue("calendar" in scopes)

    def test_working_dir(self):
        """
        Assert that the working (hidden) directory has a fluid home
        directory
        """

        home = pathlib.Path.home()

        expected_credentials = home.joinpath(".code_clinic/credentials")
        expected_calendar = home.joinpath(".code_clinic/calendar_data")

        self.assertEqual(config.DIR_CREDENTIALS, expected_credentials)
        self.assertEqual(config.DIR_CALENDAR_DATA, expected_calendar)

    def test_getting_filenames(self):
        """Assert generalised access to working filenames"""

        token_filename = config.FILENAMES["token"]
        credentials_filename = config.FILENAMES["credentials"]
        calendar_data_filename = config.FILENAMES["calendar_data"]

        self.assertTrue("token.json" in token_filename)
        self.assertTrue("credentials.json" in credentials_filename)
        self.assertTrue("calendar_data.json" in calendar_data_filename)

    @patch("pathlib.Path.exists", return_value=False)
    @patch("pathlib.Path.mkdir")
    def test_create_when_no_working_dir(self, mock_mkdir, mock_path_exists):
        """Assert a working directory is created should one be missing"""

        config.create_working_directories()
        self.assertEqual(mock_mkdir.call_count, 3)

    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.mkdir")
    def test_create_when_working_dir_present(self, mock_mkdir, mock_path_exists):
        """
        Assert no changes made to the file system should a working
        directory already exist
        """

        config.create_working_directories()
        self.assertEqual(mock_mkdir.call_count, 0)

    @patch("builtins.open")
    @patch("builtins.print")
    @patch("json.load", return_value={"expiry": "2024-04-20T06:58:16.313458Z"})
    def test_config_display(self, mock_json_load, mock_print, mock_open):
        """Assert user is shown present settings"""

        creds_path = pathlib.Path.home().joinpath(".code_clinic/credentials").as_posix()

        config.display_config()

        output = self.get_output(mock_print)

        self.assertTrue("config" in output)
        self.assertTrue("creds_path" in output)
        self.assertTrue("credentials.json" in output)
        self.assertTrue("expiry_date" in output)
        self.assertTrue("april 20, 2024" in output)
        mock_open.assert_called_once()
        mock_print.assert_called_once()

    @patch("builtins.print")
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_config_display_with_no_creds(self, mock_open, mock_print):
        """Assert user is shown present settings"""

        config.display_config()

        mock_open.assert_called_once()
        mock_print.assert_called_once_with(
            "Credentials invalid, please refet to README"
        )


if __name__ == "__main__":
    main()
