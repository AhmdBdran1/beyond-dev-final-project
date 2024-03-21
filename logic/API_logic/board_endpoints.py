import requests

from utils import read_from_secret_file


class BoardEndPoints:
    config = read_from_secret_file()
    token = config['website_token']
    api_key= config['api_key']
    # Constants for Trello API
    BASE_URL = 'https://api.trello.com/1'
    CREATE_BOARD_URL = f'{BASE_URL}/boards/'
    #api_key = "ABBAbbe530cb763d9199352c6463e3440ac8"
    #token = "ABBAATTA4f14fcd1933bde89ab95ad5f3003ae9e2c09081ad8079f39b3865259dc47671420A43297"
    #token = token[4:]  # Extract from the 4th character (index 3) to the end
    #api_key = api_key[4:]

    def create_new_board(self):
        print(self.token)
        print(self.api_key)
        # Parameters for creating a new board
        board_name = 'Ahmd bdran'
        params = {
            'key': self.api_key,
            'token': self.token,
            'name': board_name
        }

        # Make a POST request to create a new board
        response = requests.post(self.CREATE_BOARD_URL, params=params)

        return response


