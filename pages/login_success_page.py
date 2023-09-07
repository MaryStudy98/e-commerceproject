import time
from pages.base_page import BasePage
from pages.login_success_page_locators import LoginSuccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL

class LoginSuccessPage(BasePage):

    def get_login_success_label(self):
        lbl_login_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, LoginSuccessPageLocators.PRODUCT).text
        return lbl_login_success_txt

    def display_item_page(self):
        lbl_product_display_txt = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                                        LoginSuccessPageLocators.DISPLAY_FIRST_ITEM)
        # ITEM_NAME
        lbl_product_name = lbl_product_display_txt.text
        return lbl_product_name







