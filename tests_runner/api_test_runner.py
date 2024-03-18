
from infra.api_wrapper import APIWrapper
from tests.api_test.locations_test import LocationsTest
from tests.api_test.login_test import LoginTest
from tests.api_test.observations_test import ObservationsTest

def main():
    test_cases = [LoginTest, LocationsTest, ObservationsTest]
    my_api = APIWrapper()
    my_api.run_tests(test_cases)


if __name__ == "__main__":
    main()
