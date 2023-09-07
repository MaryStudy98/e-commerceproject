import time

from pages.forgot_password_link_text_page import ForgotPasswordLinkTextPage
from resources.constants import TEST_SITE_URL1


class TestLink:

    # Test Case ( Successful forgot link)
    def test_index_page(self, driver):
        forgot_password_link_text_page = ForgotPasswordLinkTextPage(driver)
        forgot_password_link_text_page.navigate_to(TEST_SITE_URL1)
        forgot_password_link_text_page.wait_and_click_link()
        time.sleep(5)