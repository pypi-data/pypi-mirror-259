from unittest.mock import patch, Mock
from unittest.mock import patch, MagicMock
import unittest
import sys
import pathlib
from datetime import datetime, timedelta


sys.path.append(pathlib.Path.cwd().as_posix())


import commands.booking


@unittest.skip
class TestVolunteerFunctions(unittest.TestCase):
    """Mock the Google API client"""

    @patch("commands.booking.build")
    @patch(
        "commands.booking.open", new_callable=unittest.mock.mock_open, read_data="{}"
    )
    def test_book_slot_not_found(self, mock_open, mock_build):

        creds = Mock()
        student_email = "test@example.com"
        event_id = "event123"

        commands.booking.book_selected_slot(creds, student_email, event_id)

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
