import time
import pytest as pytest
import softest as softest

from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    def test_search_flights_1_stop(self):
        search_flight_result = self.lp.searchFlights("New Delhi", "JFK", "24/09/2021")
        self.lp.page_scroll()
        search_flight_result.filter_flights("1 Stop")
        all_stops1 = search_flight_result.get_flight_search_result()
        print(len(all_stops1))
        time.sleep(2)
        self.ut.assertListItemText(all_stops1, "1 Stop")

    # def test_search_flights_2_stops(self):
    #     search_flight_result = self.lp.searchFlights("New Delhi", "New Jersey", "26/09/2021")
    #     self.lp.page_scroll()
    #     search_flight_result.filter_flights("2 Stops")
    #     all_stops2 = search_flight_result.get_flight_search_result()
    #     print(len(all_stops2))
    #     time.sleep(2)
    #     self.ut.assertListItemText(all_stops2, "2 Stops")
