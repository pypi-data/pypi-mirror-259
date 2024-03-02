import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime as dt
from commands.view_calendar import (
    get_code_clinic_calendar_events,
    is_update_needed,
    get_student_calendar_events,
    is_student_update_needed,
)


class TestCalendarFunctions(unittest.TestCase):
    @patch("commands.view_calendar.build")
    @patch("commands.view_calendar.config.CALENDAR_ID", "test_calendar_id")
    def test_get_code_clinic_calendar_events(self, mock_build):
        """test the retrieval of the code clinic events"""
        creds = MagicMock()
        mock_service = MagicMock()
        mock_build.return_value = mock_service

        events_data = [
            {
                "summary": "Loop",
                "start": {"dateTime": "2024-02-29T10:00:00Z"},
                "end": {"dateTime": "2024-02-29T10:30:00Z"},
            },
            {
                "summary": "Function",
                "start": {"dateTime": "2024-02-29T11:00:00Z"},
                "end": {"dateTime": "2024-02-29T11:30:00Z"},
            },
        ]
        mock_service.events().list.return_value.execute.return_value = {
            "items": events_data
        }
        events = get_code_clinic_calendar_events(creds)
        expected_events = [
            {
                "summary": "Loop",
                "start": {"dateTime": "2024-02-29T10:00:00Z"},
                "end": {"dateTime": "2024-02-29T10:30:00Z"},
            },
            {
                "summary": "Function",
                "start": {"dateTime": "2024-02-29T11:00:00Z"},
                "end": {"dateTime": "2024-02-29T11:30:00Z"},
            },
        ]
        self.assertEqual(events, expected_events)

    @patch("commands.view_calendar.cal.read_from_file")
    def test_update_needed_empty_calendar(self, mock_read_from_file):
        """test if the calendar is empty and checks if update is needed"""
        mock_read_from_file.return_value = {}
        result = is_update_needed("path/to/student_calendar.json")
        self.assertTrue(result)

    @patch("commands.view_calendar.cal.read_from_file")
    def test_update_needed_event_within_7_days(self, mock_read_from_file):
        """tests if the event within the 7 days"""
        mock_read_from_file.return_value = {
            "2024-03-01T12:00:00": "Event 1",
            "2024-03-05T14:30:00": "Event 2",
        }

        result = is_update_needed("path/to/student_calendar.json")
        self.assertTrue(result)

    @patch("commands.view_calendar.build")
    @patch("commands.view_calendar.config.CALENDAR_ID", "test_calendar_id")
    def test_get_student_calendar_events(self, mock_build):
        """test the retrieval of the student events"""
        creds = MagicMock()
        mock_service = MagicMock()
        mock_build.return_value = mock_service

        events_data = [
            {
                "summary": "Loop",
                "start": {"dateTime": "2024-02-29T10:00:00Z"},
                "end": {"dateTime": "2024-02-29T10:30:00Z"},
            },
            {
                "summary": "Function",
                "start": {"dateTime": "2024-02-29T11:00:00Z"},
                "end": {"dateTime": "2024-02-29T11:30:00Z"},
            },
        ]
        mock_service.events().list.return_value.execute.return_value = {
            "items": events_data
        }
        events = get_student_calendar_events(creds)
        expected_events = [
            {
                "summary": "Loop",
                "start": {"dateTime": "2024-02-29T10:00:00Z"},
                "end": {"dateTime": "2024-02-29T10:30:00Z"},
            },
            {
                "summary": "Function",
                "start": {"dateTime": "2024-02-29T11:00:00Z"},
                "end": {"dateTime": "2024-02-29T11:30:00Z"},
            },
        ]
        self.assertEqual(events, expected_events)

    @patch("commands.view_calendar.cal.read_from_file")
    def test_student_update_needed_empty_calendar(self, mock_read_from_file):
        """test if the student calendar is empty and checks if update is needed"""
        mock_read_from_file.return_value = {}
        result = is_student_update_needed("path/to/student_calendar.json")
        self.assertTrue(result)

    @patch("commands.view_calendar.cal.read_from_file")
    def test_student_update_needed_event_within_7_days(self, mock_read_from_file):
        """tests if the event within the 7 days"""
        mock_read_from_file.return_value = {
            "2024-03-01T12:00:00": "Event 1",
            "2024-03-05T14:30:00": "Event 2",
        }

        result = is_student_update_needed("path/to/student_student_calendar.json")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
