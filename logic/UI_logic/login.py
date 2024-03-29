from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class Login(BasePage):
    USER_INPUT_XPATH = "//input[@id='user']"
    CONTINUE_BTN_XPATH = "//input[@id='login']"
    PASSWORD_INPUT_XPATH = "//input[@id='password']"
    LOGIN_BTN_XPATH = "//button[@id='login-submit']"

    USERNAME = "vevem14@gmail.com"
    PASSWORD = "Ah2024bdr"

    # URL of the Trello login page
    LOGIN_URL = "https://trello.com/login"#h

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self):
        # Find the username and password fields and enter the credentials
        username_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.USER_INPUT_XPATH)))
        username_field.send_keys(self.USERNAME)

        continue_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BTN_XPATH)))
        continue_btn.click()

        password_field = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.PASSWORD_INPUT_XPATH)))
        password_field.send_keys(self.PASSWORD)
        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for the login process to complete
        WebDriverWait(self.driver, 10).until(EC.url_changes(self.LOGIN_URL))
        return True



