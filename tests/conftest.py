import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    user_name = "standard_user"
    password = "secret_sauce"
    wrong_user = "Janetuuuu"
    wrong_password = "Qert12@"
    return [user_name, password,wrong_user,wrong_password]

@pytest.fixture(scope="function")
def type_country_search():
    country = "India"
    return country

@pytest.fixture(scope="function")
def personal_details():
    first_name = "@=@"
    last_name = "@=@"
    zip_code = "@=@"
    return [first_name, last_name,zip_code]

@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()