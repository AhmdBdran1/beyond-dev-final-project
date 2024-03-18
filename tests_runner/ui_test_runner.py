

from tests.ui_test.test_login_page import LoginPageTests
from tests.ui_test.test_setting_page import SettingPageTests
import unittest


def suite():
    test_suite = unittest.TestSuite()
    # Add specific tests from different test classes to the suite
    test_suite.addTest(LoginPageTests('test_all_tests'))
    #test_suite.addTest(SettingPageTests('test_all_tests'))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite_to_run = suite()
    runner.run(suite_to_run)
