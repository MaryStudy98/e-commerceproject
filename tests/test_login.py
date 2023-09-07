from test_utils import *
import time
from pages.index_page import IndexPage
from pages.login_success_page import LoginSuccessPage
from resources.constants import TEST_SITE_URL, TEST_SITE_URL


class TestLogin:

    # Test Case (unsuccessful login)
    def test_login_fail(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        login_page = IndexPage(driver)
# Invalid username and valid Password
        login_page.wrong_in_type_user_name(username_password)
        login_page.type_password(username_password)
        time.sleep(5)
        login_page.click_submit_btn()
        login_failed = login_page.error_in_message()
        login_failed_text = "Epic sadface: Username and password do not match any user in this service"
        print(login_failed_text)
        assert login_failed == login_failed_text, "login failed"


    def test_valid_user_invalid_password(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        login_page = IndexPage(driver)
# Valid username and invalid password
        login_page.wait_and_type_user_name(username_password)
        login_page.wrong_in_type_password(username_password)
        time.sleep(5)
        login_page.click_submit_btn()
        login_failed = login_page.error_in_message()
        test_valid_user_invalid_password_failed_text = "Epic sadface: Username and password do not match any user in this service"
        print(test_valid_user_invalid_password_failed_text)
        assert login_failed == test_valid_user_invalid_password_failed_text

# blank username and blank password
    def test_login_no_username_no_password(self,driver):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        login_page = IndexPage(driver)
        time.sleep(5)
        login_page.click_submit_btn()
        login_failed_text = login_page.error_in_message()
        test_login_no_username_no_password_failed_text = "Epic sadface: Username is required"
        print(test_login_no_username_no_password_failed_text)
        assert login_failed_text == test_login_no_username_no_password_failed_text , "login failed"

# invalid username and invalid password
    def invalid_user_invalid_password(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        login_page = IndexPage(driver)
        login_page.wrong_in_type_user_name(username_password)
        login_page.wrong_in_type_password(username_password)
        time.sleep(5)
        login_page.click_submit_btn()
        login_failed_report = login_page.error_in_message()
        invalid_user_invalid_password_failed_text = "Epic sadface: Username and password do not match any user in this service"
        print(invalid_user_invalid_password_failed_text)
        assert login_failed_report == invalid_user_invalid_password_failed_text


 #Test case (successuful login)
    def test_login_success(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        login_page = IndexPage(driver)
        # valid username and valid Password
        login_page.wait_and_type_user_name(username_password)
        login_page.type_password(username_password)
        time.sleep(5)
        login_page.click_submit_btn()
        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        assert login_success_lbl, "user login failed"
        # Successful Login
        time.sleep(2)
        login_page.wait_and_type_user_name(username_password)
        time.sleep(2)
        login_page.pass_clear()
        login_page.type_password(username_password)
        login_page.click_submit_btn()






    # def test_inventory_page(self, driver):
    #     login_success_page = LoginSuccessPage(driver)
    #     login_success_lbl = login_success_page.get_login_success_label()
    #     login_success_lbl_text = "Products"
    #     print(login_success_lbl_text)
    #     assert login_success_lbl == login_success_lbl_text, "User Login failed!"








