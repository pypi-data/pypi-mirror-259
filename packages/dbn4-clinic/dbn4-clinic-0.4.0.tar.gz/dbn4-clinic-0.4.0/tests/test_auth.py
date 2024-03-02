"""
Test cases for cancelling a volunteer's slot
"""

from unittest.mock import MagicMock
from unittest.mock import patch
from unittest import TestCase
from unittest import main
from unittest import skip
from pathlib import Path
import warnings
import pathlib
import sys
import os


"""
Warning suppressing for the certifi.core.py DeprecationWarning
IssueTracker: https://bugs.python.org/msg414425
"""
warnings.filterwarnings("ignore", category=DeprecationWarning)
sys.path.append(pathlib.Path.cwd().as_posix())


from requests.exceptions import MissingSchema


from utils import auth


class TestAuth(TestCase):

    @staticmethod
    def get_output(mock_print):
        """Provide mocked print out as a lowercased string"""

        calls = mock_print.call_args_list
        return " ".join(str(call_.args) for call_ in calls).lower()

    @patch("utils.auth.is_creds_file", return_value=False)
    def test_no_creds_exists(self, mock_credentials):
        """Assert user is informed if no credentials found"""

        with self.assertRaises(FileNotFoundError) as error:
            auth.authenticate()

        exception = str(error.exception).lower()
        self.assertTrue("credentials not found" in exception)
        self.assertTrue("readme.md" in exception)

    @patch("builtins.open")
    @patch("utils.auth.InstalledAppFlow.from_client_secrets_file")
    @patch("utils.auth.is_token_file", return_value=False)
    @patch("utils.auth.is_creds_file", return_value=True)
    def test_no_token_exists(self, mock_credentials, mock_token, mock_flow, mock_open):
        """Assert token is created if no token found"""

        auth.authenticate()

        expected_path = Path.home().joinpath(".code_clinic/credentials/token.json")
        mock_open.assert_called_once_with(expected_path.as_posix(), "w")

    @patch("utils.auth.is_creds_valid", return_value=True)
    @patch("utils.auth.load_creds_from_file", return_value="mocked creds")
    @patch("utils.auth.is_token_file", return_value=True)
    @patch("utils.auth.is_creds_file", return_value=True)
    def test_has_token(self, mock_credentials, mock_token, mock_load, mock_valid):
        """Assert token is returned if token found"""

        self.assertEqual(auth.authenticate(), "mocked creds")

    @patch("google.oauth2.credentials.Credentials")
    @patch("requests.get")
    def test_is_connected_when_connected(self, mock_get, mock_creds):
        mock_get.return_value.return_value = True

        connected = auth.is_connected(mock_creds)

        self.assertTrue(connected)
        mock_creds.token.__str__.assert_called_once()
        mock_get.assert_called_once()

    @patch("requests.get")
    @patch("builtins.print")
    @patch("google.oauth2.credentials.Credentials")
    def test_is_connected_when_not_connected(self, mock_creds, mock_print, mock_get):
        mock_get.side_effect = MissingSchema

        connected = auth.is_connected(mock_creds)
        output = self.get_output(mock_print)

        self.assertFalse(connected)
        self.assertTrue(";( hmmm ..." in output)
        self.assertTrue("we can't talk to the calendars" in output)
        mock_get.assert_called_once()


class TestInitialisation(TestAuth):

    @patch("builtins.print")
    @patch("pathlib.Path.mkdir")
    @patch("pathlib.Path.exists", return_value=False)
    @patch("pathlib.Path.is_file", side_effects=[False, True])
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_initialisation_for_first_time(
        self, mock_open, mock_is_file, mock_exists, mock_mkdir, mock_print
    ):
        """Assert expected call count to helpers"""

        auth.initialise()
        self.assertEqual(mock_mkdir.call_count, 3)
        self.assertEqual(mock_exists.call_count, 1)

    @patch("utils.config.display_config")
    @patch("builtins.print")
    @patch("pathlib.Path.mkdir")
    @patch("pathlib.Path.exists", return_value=True)
    @patch("pathlib.Path.is_file", side_effects=[False, True])
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_initialisation_on_following_runs(
        self,
        mock_open,
        mock_is_file,
        mock_exists,
        mock_mkdir,
        mock_print,
        mock_display_config,
    ):
        """Assert expected call count to helpers"""

        auth.initialise()
        mock_display_config.assert_called_once()
        self.assertEqual(mock_mkdir.call_count, 0)
        self.assertEqual(mock_exists.call_count, 1)
        self.assertEqual(mock_is_file.call_count, 1)

    @skip
    @patch("builtins.print")
    @patch("pathlib.Path.mkdir")
    @patch("pathlib.Path.exists")
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_initialisation_user_guide(
        self, mock_open, mock_exists, mock_mkdir, mock_print
    ):
        """Assert expected to wait for user to provide a `credetials.json` file"""

        mock_exists.side_effects = [False, False, False, True]
        auth.initialise()

        output = self.get_output(mock_print)

        self.assertTrue("let's get you set up" in output)
        self.assertTrue("for ease of use" in output)
        self.assertTrue("please follow along with the readme" in output)

        output = self.get_output(mock_print)

        self.assertTrue("and here we go ^_^" in output)


if __name__ == "__main__":
    main()
