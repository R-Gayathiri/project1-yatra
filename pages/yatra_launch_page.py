import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bases.base_driver import BaseDriver
from pages.search_results_page import SearchFlightResults


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "BE_flight_arrival_city"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    DEPARTURE_DATE = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def getdepartfromfield(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getgoingtofield(self):
        return self.wait_element_to_be_clickable(By.ID, self.GOING_TO_FIELD)

    def getgoingtoresults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getdeparturedatefield(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.DEPARTURE_DATE)

    def getalldatefields(self):
        return self.wait_element_to_be_clickable(By.XPATH, self.ALL_DATES)

    def getsearchbutton(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def enterdepartfromlocation(self, departlocation):
        self.getdepartfromfield().click()
        self.getdepartfromfield().send_keys(departlocation)
        self.getdepartfromfield().send_keys(Keys.ENTER)
        time.sleep(2)

    def entergoingtolocation(self, goingtolocation):
        self.getgoingtofield().click()
        self.getgoingtofield().send_keys(goingtolocation)
        search = self.getgoingtoresults()
        time.sleep(2)
        for results in search:
            if goingtolocation in results.text:
                results.click()
                break

    def enterdeparturedate(self, departuredate):
        self.getdeparturedatefield().click()
        all_dates = self.getalldatefields().find_elements(By.XPATH, self.ALL_DATES)
        for dates in all_dates:
            if dates.get_attribute("data-date") == departuredate:
                dates.click()
                break

    def clicksearchbutton(self):
        self.getsearchbutton().click()
        time.sleep(3)

    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterdepartfromlocation(departlocation)
        self.entergoingtolocation(goingtolocation)
        self.enterdeparturedate(departuredate)
        self.clicksearchbutton()
        search_flights_result = SearchFlightResults(self.driver)
        return search_flights_result
