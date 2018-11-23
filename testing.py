"""testing.py"""

import unittest
from passwordtester import password_checker


PASSWORD_LIST = ['ABd1234@1', 'a F1#', '2w3E*', '2We3345']
SEARCH = r"\w+\W+\s*"


class BaseTestCase(unittest.TestCase):
    """Test class for Password checker of program"""
    def test_instance_input(self):
        """Test if input is a sequence or not"""
        self.assertIsInstance(PASSWORD_LIST, list, msg='Parameter is not a list')

    def test_short_length(self):
        """tests for shorter length value"""
        output = password_checker(PASSWORD_LIST)
        self.assertGreaterEqual(len(output), 6, msg="Value should be in range 6-12 ")

    def test_longer_length(self):
        """tests for longer length value"""
        output = password_checker(PASSWORD_LIST)
        self.assertLessEqual(len(output), 12, msg="Value should be in range 6-12")

    def test_string_in_password(self):
        """test for string in password"""
        output = password_checker(PASSWORD_LIST)
        self.assertRegexpMatches(output, SEARCH, msg='Password should contain a-zA-Z0-9@#$$and whitespace')


if __name__ == '__main__':
    unittest.main()
