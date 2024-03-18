import json
from time import sleep

from jira import JIRA
from selenium import webdriver
import os
import concurrent.futures

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def read_config(file_path):  # open the config file for read
    script_directory = os.path.dirname(os.path.realpath(__file__))
    absolute_path = os.path.join(script_directory, file_path)
    with open(absolute_path, 'r') as f:
        config = json.load(f)
    return config


class BrowserWrapper:
    def __init__(self):
        self.driver = None

    def get_driver(self, option):  # create driver based on config content
        config_file = '../config.json'
        config = read_config(config_file)
        grid = config['grid']
        hub_url = config['hub_url']
        url = config['url']
        option.add_argument('--headless')  # This line makes Chrome run in headless mode
        option.add_argument('--no--sandbox')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--window-size=1920x1080')

        if grid:
            print('ala ala')
            print(option.to_capabilities())
            driver = webdriver.Remote(command_executor=hub_url, options=option)
            driver.get(url)
            # Wait until the title changes from "Just a moment..."
            print(f"{driver.title} hada hoo")
            driver.maximize_window()
            return driver
        else:
            print('bla bla')
            driver = webdriver.Chrome(option)
            driver.get(url)
            print(f"{driver.title} hada hoo")

            driver.maximize_window()
            return driver

    def test_run_grid_serial(self, test_execute):  # run the test with serial processs
        cap_list = self.get_capabilities_list()
        for caps in cap_list:
            test_execute(caps)

    def test_run_grid_parallel(self, test_execute):
        options_list = self.get_capabilities_list()
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(options_list)) as executor:
            list(executor.map(test_execute, options_list))

    def run_test(self, test_execute):
        config_file = '../config.json'
        config = read_config(config_file)
        grid = config['grid']
        if grid:
            self.test_run_grid_parallel(test_execute)
        else:
            self.test_run_grid_serial(test_execute)

    def get_capabilities_list(self):  # initialize the capabilities we need to test on
        chrome_cap = webdriver.ChromeOptions()
        firefox_cap = webdriver.FirefoxOptions()
        cap_list = [firefox_cap, chrome_cap]
        return cap_list
