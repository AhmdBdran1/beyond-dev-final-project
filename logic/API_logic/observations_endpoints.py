import utils


class ObservationsEndpoints:
    def __init__(self, my_api, token):
        self.my_api = my_api
        self.token = token
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def get_user_observations(self):
        endpoints = "observations/?page=1&page_size=10"
        response = self.my_api.api_get_request(endpoints, self.headers)
        return response

    def add_new_observation(self, location_id, owner_id):
        endpoints = "observations/"
        data = utils.get_observation_data_as_json(location_id, owner_id)
        response = self.my_api.api_post_request(endpoints, data, self.headers)
        return response

    def get_observation_by_id(self, observation_id):
        endpoints = f"observations/{observation_id}"
        response = self.my_api.api_get_request(endpoints, self.headers)
        return response

    def update_observation_data(self, observation_id, location_id, owner_id):
        endpoints = f"observations/{observation_id}"
        data = utils.get_observation_data_as_json_for_updating(observation_id, location_id, owner_id)
        response = self.my_api.api_put_request(endpoints, data, self.headers)
        return response

    def delete_observation_data(self, observation_id):
        endpoints = f"observations/{observation_id}"
        response = self.my_api.api_delete_request(endpoints, self.headers)
        return response
