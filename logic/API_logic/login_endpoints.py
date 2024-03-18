from utils import read_config


class LoginEndpoints:
    def __init__(self, my_api):
        self.my_api = my_api
        config = read_config()
        self.email = config['email']
        self.password = config['password']

    def perform_login(self):
        # Define the URL
        endpoints = "users/login"

        data = {
            "email": self.email,
            "password": self.password
        }

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        response = self.my_api.api_post_request(endpoints, data, headers)
        return response
