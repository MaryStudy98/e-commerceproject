from resources.constants import TEST_SITE_URLA


class TestFightLogin:

    def test_flight_page(self, driver):
        flight_booking_page = flight_booking_page(driver)
        flight_booking_page.navigate_to(TEST_SITE_URLA)
        login_page = Page(driver)

        login_page.click_submit_btn()