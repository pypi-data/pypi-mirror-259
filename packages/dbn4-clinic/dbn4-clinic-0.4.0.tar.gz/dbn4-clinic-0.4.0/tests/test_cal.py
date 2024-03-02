"""
Test cancellation of `cal` utility
"""

from unittest.mock import patch
from unittest import TestCase
from unittest import main
from unittest import skip
import pathlib
import json
import sys


sys.path.append(pathlib.Path.cwd().as_posix())


from utils import cal


class TestIsBooked(TestCase):
    
    @skip
    def test_when_is_booked(self):
        """Assert event is booked when attendee is not volunteer"""

        with open("tests/data/mock_booked_event.json") as file:
            mock_event = json.load(file)

        user_email = "person_one@student.wethinkcode.co.za"
        result = cal.is_booked(user_email, mock_event)

        self.assertTrue(result)

    def test_when_is_not_booked_no_attendees_logged(self):
        """Assert event with no attendees attached is regarded as unbooked"""

        with open("tests/data/mock_unbooked_event.json") as file:
            mock_event = json.load(file)

        user_email = "person_zero@student.wethinkcode.co.za"
        result = cal.is_booked(user_email, mock_event)

        self.assertFalse(result)


class TestIsCreator(TestCase):

    def test_when_is_creator(self):
        """Assert when user is event creator"""

        with open("tests/data/mock_booked_event.json") as file:
            mock_event = json.load(file)

        user_email = "person_zero@student.wethinkcode.co.za"
        result = cal.is_creator(user_email, mock_event)

        self.assertTrue(result)

    def test_when_is_incorrect_creator(self):
        """Assert when user is event creator"""

        with open("tests/data/mock_unbooked_event.json") as file:
            mock_event = json.load(file)

        user_email = "person_two@student.wethinkcode.co.za"
        result = cal.is_creator(user_email, mock_event)

        self.assertFalse(result)


@skip
class TestMakeUserSelection(TestCase):

    @patch("builtins.input")
    def test_input_less_than_one(self, mock_input):
        mock_input.side_effects = ["-1", "0", "1"]
        selection = cal.make_user_selection(max_num=5)

        self.assertEqual(selection, 1)

    @patch("builtins.input")
    def test_input_more_than_max(self, mock_input):
        mock_input.side_effects = ["7", "6", "5"]
        selection = cal.make_user_selection(max_num=5)

        self.assertEqual(selection, 1)


if __name__ == "__main__":
    main()
