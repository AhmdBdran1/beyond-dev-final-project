import utils


class LocationsEndpoints:

    def __init__(self, my_api, token):
        self.my_api = my_api
        self.token = token
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    def get_user_locations(self):
        endpoints = "locations/?page=1&page_size=10"
        response = self.my_api.api_get_request(endpoints, self.headers)
        return response

    def add_new_location(self, owner_id):
        endpoints = "locations/"
        # Generate random values for latitude, longitude, datetime
        latitude, longitude = utils.generate_random_coordinates()
        datetime_value = utils.generate_random_datetime()

        data = {
            "id": utils.generate_random_object_id(),
            "street_address": "123 Observatory Lane",
            "country": "Israel",
            "lng": longitude,
            "updated_at": datetime_value,
            "short_name": "Observatory Lane",
            "owner": owner_id,
            "alt": 1500,
            "lat": latitude
        }

        response = self.my_api.api_post_request(endpoints, data, self.headers)
        return response

    def get_location_by_id(self, location_id):
        endpoints = f"locations/{location_id}"
        response = self.my_api.api_get_request(endpoints, self.headers)
        return response

    def update_a_location(self, location_id):
        endpoints = f"locations/{location_id}"
        response = self.get_location_by_id(location_id)
        data = response.json()
        data = {
            "id": data['id'],
            "street_address": data['street_address'],
            "country": "updated",
            "lng": data['lng'],
            "updated_at": data['updated_at'],
            "short_name": data['short_name'],
            "owner": data['owner'],
            "alt": data['alt'],
            "lat": data['lat']
        }

        response = self.my_api.api_put_request(endpoints, data, self.headers)
        return response

    def delete_location(self, location_id):
        endpoints = f"locations/{location_id}"
        response = self.my_api.api_delete_request(endpoints, self.headers)
        return response

