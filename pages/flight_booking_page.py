from pages.base_page import BasePage
from pages.flight_booking_page_locators import FlightBookingPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class FlightBookingPage(BasePage):

    def get_flight_page(self):
        flight= self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, FlightBookingPageLocators.LOGO).text
        return flight

