import requests


class BoardEndPoints:
    # Constants for Trello API
    BASE_URL = 'https://api.trello.com/1'
    CREATE_BOARD_URL = f'{BASE_URL}/boards/'
    api_key = "bbe530cb763d9199352c6463e3440ac8"
    token = "ATTA4f14fcd1933bde89ab95ad5f3003ae9e2c09081ad8079f39b3865259dc47671420A43297"


    def create_new_board(self):
        # Parameters for creating a new board
        board_name = 'Ahmd BB'
        params = {
            'key': self.api_key,
            'token': self.token,
            'name': board_name
        }

        # Make a POST request to create a new board
        response = requests.post(self.CREATE_BOARD_URL, params=params)

        return response


