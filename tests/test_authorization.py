from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from const import Constants


class TestAuthorization:
    def test_authorization_using_the_Login_to_account_button(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.TEST_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON, 'Оформить заказ'))

    def test_authorization_using_the_Personal_Account_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.TEST_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON, 'Оформить заказ'))

    def test_authorization_by_button_in_the_registration_form(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_TO_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION))
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.TEST_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON, 'Оформить заказ'))

    def test_authorization_using_the_button_in_the_password_recovery_form(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.RECOVER_THE_PASSWORD_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.RECOVER_THE_PASSWORD))
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.TEST_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.CHECKOUT_BUTTON, 'Оформить заказ'))




