import unittest

from selenium import webdriver

from infra.browser_wraper import BrowserWrapper
from logic.UI_logic.login import Login
from utils import create_jira_issue


class LoginPageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()

    def tearDown(self):
        # Check if the test failed
        if hasattr(self, '_outcome') and self._outcome.result:
            result = self._outcome.result

    def test_login(self, option=webdriver.ChromeOptions()):  # test the login processs
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        self.assertTrue(login_page.login())


if __name__ == "__main__":
    for i in range(10):
        unittest.main()
