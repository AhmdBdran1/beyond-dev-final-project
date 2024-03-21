from infra.browser_wraper import BrowserWrapper
from logic.API_logic.board_endpoints import BoardEndPoints
from utils import read_config
import unittest
from infra.api_wrapper import APIWrapper
from logic.API_logic.login_endpoints import LoginEndpoints


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints()

    def test_add_new_board(self):
        response = self.board_endpoint.create_new_board()
        data = response.json()
        self.assertTrue(response.status_code == 200)


if __name__ == "__main__":
    unittest.main()
