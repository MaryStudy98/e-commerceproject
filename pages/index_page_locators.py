from selenium.webdriver.common.by import By


class IndexPageLocators:

    USERNAME = (By.XPATH, "//*[@id='user-name']")
    PASSWORD = (By.XPATH, "//*[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='login-button']")
    ERROR_IN_MSG = (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]")
    ERROR_IN_BUTTON = (By.CLASS_NAME, "error-button")
    PRODUCT_LABEL_SUCCESS_LOGIN = (By.CSS_SELECTOR, "#header_container > div.header_secondary_container > span")
