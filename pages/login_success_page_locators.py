from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginSuccessPageLocators(BasePage):
    LOGIN_SUCCESS_TEXT = (By.XPATH, "//*[@id='header_container']/div[1]/div[2]/div")
    PRODUCT = (By.CLASS_NAME, "title")
    DISPLAY_FIRST_ITEM = (By.CSS_SELECTOR, "div.inventory_item:nth-child(1) div.inventory_item_name")





