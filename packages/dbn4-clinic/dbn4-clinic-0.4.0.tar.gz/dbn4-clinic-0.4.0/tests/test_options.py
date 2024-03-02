"""Test UI functionality"""

from unittest.mock import MagicMock
from unittest.mock import patch
from unittest import TestCase
from unittest import main
from unittest import skip


from commands.options import cmd_invalid
from commands.options import cmd_program_exit
from commands.options import display_options
from commands.options import get_description
from commands.options import get_options
from commands.options import execute


class TestOptions(TestCase):

    def setUp(self):
        self.expected_options = [
            "view clinic calendar",
            "view personal calendar",
            "book assistance",
            "volunteer assistance",
            "cancel assistance session",
            "cancel volunteer session",
            "configure",
            "validate connection",
            "exit",
        ]

    @staticmethod
    def get_output(mock_print):
        """Provide mocked print out as a lowercased string"""

        calls = mock_print.call_args_list
        return " ".join(str(call_.args) for call_ in calls).lower()


class TestExistanceOfOptions(TestOptions):

    @patch("builtins.print")
    def test_display_options(self, mock_print):
        """Assert call count to print function when displaying UI"""

        display_options()

        output = self.get_output(mock_print)
        call_count = len(mock_print.mock_calls)

        self.assertEqual(call_count, 2)

        for expected in self.expected_options:
            self.assertTrue(expected in output)

    def test_get_options(self):
        """Assert option/description pair in structure of data"""

        options = get_options()

        for option in options.values():
            are_valid_keys = (
                "option" in option.keys() and "description" in option.keys()
            )
            self.assertTrue(are_valid_keys)

            is_option = option["option"].lower() in self.expected_options
            self.assertTrue(is_option)

    def test_get_description(self):
        """Assert UI options are as expected"""
        description = get_description().lower()

        for expected in self.expected_options:
            self.assertTrue(expected in description)


@skip
class TestExecutingOptions(TestOptions):
    """test being performed on imported functions"""

    def setUp(self):
        self.commands = [
            ("1", "view_code_clinic_calendar"),
            ("2", "view_student_calendar"),
            ("3", "book"),
            ("4", "volunteer_assistance"),
            ("5", "cmd_cancel_assistance_session"),
            ("6", "cmd_cancel_volunteer_session"),
            ("7", "is_connected"),
            ("8", "display_config"),
            ("9", "program_exit"),
        ]

    @skip
    def test_commands_are_executed(self):
        """Assert executability of UI linked functions"""

        creds = MagicMock()

        for option, command in self.commands:
            with patch(f"commands.options.{command}") as cmd:
                execute(option, MagicMock())

            cmd.assert_called_once()

    @patch("builtins.print")
    def test_cmd_invalid(self, mock_print):
        invalid_options = ["", "invalid", "x29", "-1", 0]

        for option in invalid_options:
            cmd_invalid(option)

        output = self.get_output(mock_print)

        for option in invalid_options:
            self.assertTrue(f"no such option: '{option}'" in output)
            self.assertTrue("please select again" in output)

    @patch("builtins.print")
    def test_cmd_exit(self, mock_print):
        with self.assertRaises(SystemExit):
            cmd_program_exit()

        output = self.get_output(mock_print)

        self.assertTrue("goodbye" in output)


if __name__ == "__main__":
    main()
