import pytest
from selenium import webdriver
from const import Constants
from const import Url
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Url.URL)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER))
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.TEST_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON, 'Оформить заказ'))
    return driver
