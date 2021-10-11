import time
from selenium.webdriver.common.by import By
from bases.base_driver import BaseDriver


class SearchFlightResults(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    FILTER_BY_ONE_STOP = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_TWO_STOP = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULT = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(), '2 Stop')"

    def get_filter_by_one_stop(self):
        self.driver.find_element(By.XPATH, self.FILTER_BY_ONE_STOP)

    def get_filter_by_two_stop(self):
        self.driver.find_element(By.XPATH, self.FILTER_BY_TWO_STOP)

    def get_filter_by_NON_stop(self):
        self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP)

    def get_flight_search_result(self):
        self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULT)

    def filter_flights(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop().click()
            print("selected flights with 1 stop")
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop().click()
            print("selected flights with 2 stop")
            time.sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_NON_stop().click()
            print("selected flights with non stop")
            time.sleep(2)
        else:
            print("Please provide valid selection")
