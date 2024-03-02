import unittest
import re
from utils.check_input_error import *


@unittest.skip
class TestValidationFunctions(unittest.TestCase):
    def test_validate_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("test@.com"))
        self.assertFalse(validate_email("testexample.com"))

    def test_validate_time(self):
        self.assertTrue(validate_time("23:59"))
        self.assertFalse(validate_time("24:00"))
        self.assertFalse(validate_time("23:60"))
        self.assertFalse(validate_time("00:60"))
        self.assertFalse(validate_time("24:00"))


if __name__ == "__main__":
    unittest.main()
