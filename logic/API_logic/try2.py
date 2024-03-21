import requests

# Constants for Trello API
BASE_URL = 'https://api.trello.com/1'
CREATE_BOARD_URL = f'{BASE_URL}/boards/'

def create_new_board(api_key, token):
    # Parameters for creating a new board
    board_name = 'My New Board'
    params = {
        'key': api_key,
        'token': token,
        'name': board_name
    }

    # Make a POST request to create a new board
    response = requests.post(CREATE_BOARD_URL, params=params)

    # Check if the request was successful
    if response.ok:
        board_data = response.json()
        print("New board created successfully!")
        print("Board ID:", board_data['id'])
        print("Board Name:", board_data['name'])
        # Add more board details as needed
    else:
        print("Failed to create board. Status code:", response.status_code)
        print("Error message:", response.text)

def main():
    # Replace 'YOUR_API_KEY' and 'YOUR_TOKEN' with your actual API key and token
    api_key = "bbe530cb763d9199352c6463e3440ac8"
    token = "ATTA4f14fcd1933bde89ab95ad5f3003ae9e2c09081ad8079f39b3865259dc47671420A43297"
    create_new_board(api_key, token)

if __name__ == "__main__":
    main()
