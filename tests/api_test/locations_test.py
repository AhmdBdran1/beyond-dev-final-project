from logic.API_logic.locations_endpoints import LocationsEndpoints
from utils import read_config
import unittest
from infra.api_wrapper import APIWrapper
from logic.API_logic.login_endpoints import LoginEndpoints


class LocationsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.login_endpoint = LoginEndpoints(self.my_api)
        config = read_config()
        self.email = config['email']
        response = self.login_endpoint.perform_login()
        self.data = response.json()
        self.token = self.data["access_token"]
        self.locations_endpoints = LocationsEndpoints(self.my_api, self.token)
        self.owner_id = self.data["id"]
        self.response = self.locations_endpoints.add_new_location(self.owner_id)
        self.data = self.response.json()
        self.location_id = self.data['id']

    def tearDown(self):
        self.locations_endpoints.delete_location(self.location_id)

    def test_get_user_locations(self):
        response = self.locations_endpoints.get_user_locations()
        self.assertTrue(response.status_code == 200)

    def test_add_new_location(self):
        self.assertTrue(self.response.status_code == 201)
        self.assertEqual(self.response.json()['country'], 'Israel')

    def test_get_location_by_id(self):
        response = self.locations_endpoints.get_location_by_id(self.location_id)
        self.assertTrue(response.status_code == 200)
        self.assertEqual(response.json()['country'], 'Israel')

    def test_update_location(self):
        update_response = self.locations_endpoints.update_a_location(self.location_id)
        get_response = self.locations_endpoints.get_location_by_id(self.location_id)
        data = get_response.json()
        self.assertTrue(update_response.status_code == 204)
        self.assertEqual(data['country'], "updated")

    def test_delete_location(self):
        delete_response = self.locations_endpoints.delete_location(self.location_id)
        self.assertTrue(delete_response.status_code == 204)
