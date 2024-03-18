from logic.API_logic.locations_endpoints import LocationsEndpoints
from logic.API_logic.observations_endpoints import ObservationsEndpoints
from utils import read_config
import unittest
from infra.api_wrapper import APIWrapper
from logic.API_logic.login_endpoints import LoginEndpoints


class ObservationsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.login_endpoint = LoginEndpoints(self.my_api)
        config = read_config()
        self.email = config['email']
        response = self.login_endpoint.perform_login()
        data = response.json()
        self.owner_id = data['id']
        self.token = data["access_token"]
        self.observations_endpoints = ObservationsEndpoints(self.my_api, self.token)
        self.locations_endpoints = LocationsEndpoints(self.my_api, self.token)
        add_new_location_response = self.locations_endpoints.add_new_location(self.owner_id)
        self.location_id = add_new_location_response.json()['id']
        self.add_response = self.observations_endpoints.add_new_observation(self.location_id, self.owner_id)
        self.observation_id = self.add_response.json()['id']

    def tearDown(self):
        self.observations_endpoints.delete_observation_data(self.observation_id)
        self.locations_endpoints.delete_location(self.location_id)

    def test_get_user_observations(self):
        response = self.observations_endpoints.get_user_observations()
        self.assertTrue(response.status_code == 200)

    def test_add_new_observation(self):
        self.assertTrue(self.add_response.status_code == 201)

    def test_get_observation_by_id(self):
        get_response = self.observations_endpoints.get_observation_by_id(self.observation_id)
        self.assertTrue(get_response.status_code == 200)
        self.assertEqual(get_response.json()['id'], self.observation_id)

    def test_update_observation(self):
        update_response = self.observations_endpoints.update_observation_data(
            self.observation_id, self.location_id, self.owner_id)
        get_response = self.observations_endpoints.get_observation_by_id(self.observation_id)
        comment = get_response.json()['comment']
        self.assertTrue(update_response.status_code == 204)
        self.assertEqual(comment, 'updated')

    def test_delete_observation(self):
        delete_response = self.observations_endpoints.delete_observation_data(self.observation_id)
        self.assertTrue(delete_response.status_code == 204)
