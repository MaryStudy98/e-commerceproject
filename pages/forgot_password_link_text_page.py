from pages.base_page import BasePage

from pages.forgot_password_link_text_page_locators import PasswordLinkTextPageLocators
from resources.constants import MAX_WAIT_INTERVAL

class ForgotPasswordLinkTextPage(BasePage):

    def wait_and_click_link(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,PasswordLinkTextPageLocators.FORGOT_PASSWORD).click()