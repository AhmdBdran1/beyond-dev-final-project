import unittest
from selenium import webdriver
from infra.browser_wraper import BrowserWrapper
from logic.UI_logic.home_page import HomePage
from logic.UI_logic.login_page import LoginPage
from logic.UI_logic.main_page import MainPage
from utils import create_jira_issue


class LoginPageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()

    def tearDown(self):
        # Check if the test failed
        if hasattr(self, '_outcome') and self._outcome.result:
            result = self._outcome.result
            if result.errors or result.failures:
                # If test fails, create a JIRA issue
                test_method_name = self._testMethodName
                error_message = ""
                for test, traceback_text in result.errors + result.failures:
                    error_message += f"Test: {test}\n"
                    error_message += f"Error: {traceback_text}\n"
                create_jira_issue(f"{test_method_name} Test Failed", error_message)

    def test_login(self, option=webdriver.ChromeOptions()):  # test the login process
        driver = self.browser_wrapper.get_driver(option)
        main_page = MainPage(driver)
        main_page.click_to_start_login()
        login_page = LoginPage(driver)
        login_page.login()
        home_page = HomePage(driver)
        name = home_page.get_the_name_of_the_account_owner()
        driver.quit()
        self.assertEqual(name, "Aahmd Bdran")

    def test_specific_test(self):
        self.browser_wrapper.run_test(self.test_login)  # select the specific function you want to run

    def test_all_tests(self):  # run all tests
        tests_list = [self.test_login]
        for test in tests_list:
            self.browser_wrapper.run_test(test)


if __name__ == "__main__":
    unittest.main()