from pages.base_page import BasePage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class IndexPage(BasePage):
    def wait_and_type_user_name(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.USERNAME).send_keys(
            usr_and_pw[0])

    def type_password(self, usr_and_pw):

        self.find_element(IndexPageLocators.PASSWORD).send_keys(
            usr_and_pw[1])

    def click_submit_btn(self):
        self.find_element(IndexPageLocators.LOGIN_BUTTON).click()

    def wrong_in_type_user_name(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.USERNAME).send_keys(
            usr_and_pw[2])

    def wrong_in_type_password(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.PASSWORD).send_keys(
            usr_and_pw[3])

    def error_in_message(self):
        login_failed = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.ERROR_IN_MSG)
        login_failed_text = login_failed.text
        return login_failed_text

    def error_in_button_click(self):
        self.find_element(IndexPageLocators.ERROR_IN_BUTTON).click()

    def user_clear(self):
        username = self.find_element(IndexPageLocators.USERNAME)
        username.clear()

    def pass_clear(self):
        password = self.find_element(IndexPageLocators.PASSWORD)
        password.clear()

    def get_login_success_title(self):
        title = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,IndexPageLocators.PRODUCT_LABEL_SUCCESS_LOGIN).text
        return title

