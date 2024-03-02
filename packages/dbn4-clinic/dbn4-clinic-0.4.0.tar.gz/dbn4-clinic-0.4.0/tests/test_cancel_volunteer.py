"""
Test cancellation of volunteered slots
"""

from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import call
from unittest import TestCase
from unittest import main
from unittest import skip
import pathlib
import json
import sys


sys.path.append(pathlib.Path.cwd().as_posix())


from googleapiclient.errors import HttpError


from commands.cancel_volunteer import cancel_volunteer


class TestCancelVolunteer(TestCase):

    @patch("googleapiclient.discovery.build")
    def setUp(self, mock_build):
        """
        Prototype Google's api client discovery without interacting with
        any local version, functions or methods related to `build`
        """

        self.service = mock_build()

    @staticmethod
    def get_output(mock_print):
        """Provide mocked print out as a lowercased string"""

        calls = mock_print.call_args_list
        return " ".join(str(call_.args) for call_ in calls).lower()


class TestDeleteEvent(TestCancelVolunteer):

    @skip
    @patch("builtins.input", return_value="1")
    @patch("utils.make_user_selection", return_value=1)
    @patch("utils.read_from_file")
    @patch("utils.update_local_db")
    @patch("googleapiclient.discovery.build")
    @patch("commands.cancel_volunteer.delete_event", return_value=True)
    @patch("commands.cancel_volunteer.parse_events", return_value=(MagicMock(), MagicMock()))
    def test_deletion_returns_true(
        self,
        mock_get_deletable_events,
        mock_delete_event,
        mock_build,
        mock_write_into_file,
        mock_read_from_file,
        mock_make_user_selection,
        mock_input,
    ):
        """Assert api returns true when all goes without a hitch"""

        expected = (
            call.return_value.events.return_value.delete.return_value.execute.return_value
        )

        mock_build.return_value.events.return_value.delete.return_value.execute.return_value = (
            ""
        )
        mock_service = mock_build()
        mock_email = "person_zero@student.wethinkcode.co.za"

        is_cancelled = cancel_volunteer(
            creds=None, service=mock_service, user_email=mock_email
        )

        mock_read_from_file.assert_called_once()
        mock_write_into_file.assert_called_once()

        self.assertTrue(expected in mock_build.mock_calls)
        self.assertTrue(is_cancelled)

    @skip
    @patch("builtins.print")
    @patch("googleapiclient.discovery.build")
    @patch("commands.cancel_volunteer.get_user_email", return_value=None)
    @patch("utils.is_connected", return_value=True)
    def test_http_error_informs_user(
        self, mock_conn, mock_get_user_email, mock_build, mock_print
    ):
        """Assert user is informed where http error occurs when calling api"""

        content = b'{\n "error": {\n  "errors": [\n   {\n    "domain": "global",\n    "reason": "deleted",\n    "message": "Resource has been deleted"\n   }\n  ],\n  "code": 410,\n  "message": "Resource has been deleted"\n }\n}\n'
        resp = MagicMock(reason="")

        error = HttpError(resp, content)

        mock_build.return_value.events.return_value.delete.return_value.execute.side_effect = (
            error
        )
        mock_service = mock_build()

        mock_event_id = None
        mock_creds = None

        expected = call().events().delete().execute()

        is_cancelled = cancel_volunteer(mock_creds, mock_service, mock_event_id)

        output = self.get_output(mock_print)

        self.assertTrue("hmmm ... according to our friends at google" in output)
        self.assertTrue("please consider double checking for us" in output)

        self.assertFalse(is_cancelled)
        self.assertTrue(expected in mock_build.mock_calls)

        mock_conn.assert_called_once_with(mock_creds)
        mock_can_be_deleted.assert_called_once_with(mock_event_id, mock_service)


if __name__ == "__main__":
    main()
