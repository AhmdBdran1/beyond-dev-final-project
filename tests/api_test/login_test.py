from infra.browser_wraper import BrowserWrapper
from utils import read_config
import unittest
from infra.api_wrapper import APIWrapper
from logic.API_logic.login_endpoints import LoginEndpoints


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.login_endpoint = LoginEndpoints(self.my_api)
        config = read_config()
        self.email = config['email']
        self.browser_wrapper = BrowserWrapper()

    def test_login(self):
        response = self.login_endpoint.perform_login()
        data = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertEqual(data["email"], self.email)

