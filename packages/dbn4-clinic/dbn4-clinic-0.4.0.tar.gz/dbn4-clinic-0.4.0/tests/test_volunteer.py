import unittest
from unittest.mock import patch, MagicMock
from commands.volunteer import *

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import pytz
from utils.cal import is_working_day


@unittest.skip
class TestCalendarFunctions(unittest.TestCase):

    def test_is_working_day(self):
        # Test if a given date is a working day (Monday to Friday)
        self.assertTrue(is_working_day(2023, 4, 14))  # Assuming this is a Friday
        self.assertFalse(is_working_day(2023, 4, 15))  # Assuming this is a Saturday

    # @patch('commands.volunteer.is_slot_available', return_value=False)
    @patch("commands.volunteer.create_event")
    def test_volunteer_slot_unavailable(
        self, mock_create_event
    ):  # , mock_is_slot_available):
        # Test booking a slot when it is unavailable
        creds = MagicMock()
        volunteer_slot(
            creds,
            2023,
            4,
            14,
            "10:00",
            "Test Description",
            "test@student.wethinkcode.co.za",
        )
        mock_create_event.assert_not_called()


if __name__ == "__main__":
    unittest.main()
