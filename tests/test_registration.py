from faker import Faker
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

fake = Faker()


class TestRegistration:
    def test_successful_registration(self, driver):
        name = fake.name()
        email = fake.email()
        password = fake.password()
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_TO_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION))
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(Locators.ENTER))
        assert '/login' in driver.current_url

    def test_registration_with_empty_name(self, driver):
        email = fake.email()
        password = fake.password()
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_TO_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert '/login' not in driver.current_url

    def test_registration_with_5_symbols(self, driver):
        password = 'abc45'
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.REGISTRATION_TO_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION))
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.EMAIL_FIELD).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.INVALID_PASSWORD_MESSAGE))






