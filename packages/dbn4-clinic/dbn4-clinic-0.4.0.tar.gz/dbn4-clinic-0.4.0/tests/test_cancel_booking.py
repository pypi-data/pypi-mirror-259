import unittest
from unittest.mock import patch, MagicMock, mock_open
from io import StringIO
import commands.cancel_booking

from datetime import datetime
import pathlib
import sys

sys.path.append(pathlib.Path.cwd().as_posix())

import utils
from commands.cancel_booking import HttpError


@unittest.skip
class TestCancelBooking(unittest.TestCase):
    @patch("builtins.print")
    @patch("utils.read_from_file", return_value={})
    def test_cancel_booking_slot_not_found(self, mock_read_from_file, mock_print):
        service = MagicMock()
        student_email = "test@example.com"

        commands.cancel_booking.cancel_booking(service, student_email)

        mock_print.assert_called_once_with("You have no booking sessions to cancel.")
        mock_read_from_file.assert_called_once_with(utils.CALENDAR_DATA)

    @patch("commands.cancel_booking.utils.read_from_file")
    def test_extract_removeable_events(self, mock_read_from_file):
        """tests that the function correctly filters out events that the student can cancel"""
        student_email = "student@example.com"
        events = {
            "2024-03-01": {
                "attendees": ["student@example.com"],
                "id": "event_id_1",
                "creator": "creator@example.com",
            },
            "2024-03-02": {"attendees": ["another@example.com"], "id": "event_id_2"},
            "2024-03-03": {"id": "event_id_3"},
        }
        mock_read_from_file.return_value = events
        result = commands.cancel_booking.extract_removeable_events(
            student_email, events
        )
        expected_result = {
            "2024-03-01": {
                "attendees": ["student@example.com"],
                "id": "event_id_1",
                "creator": "creator@example.com",
            }
        }
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
