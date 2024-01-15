from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPersonalAccount:
    def test_go_to_personal_account(self, login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        assert WebDriverWait(login, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PERSONAL_ACCOUNT_TEXT, 'В этом разделе вы '
                                                                                              'можете изменить свои '
                                                                                              'персональные данные'))

    def test_go_to_constructor_from_personal_account(self, login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_TEXT))
        login.find_element(*Locators.CONSTRUCTOR_LINK).click()
        assert WebDriverWait(login, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.BURGER_TEXT, 'Соберите бургер'))

    def test_go_to_constructor_from_personal_account_by_logo_button(self, login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_TEXT))
        login.find_element(*Locators.LOGO_BUTTON).click()
        assert WebDriverWait(login, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.BURGER_TEXT, 'Соберите бургер'))

    def test_logout(self, login):
        login.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.PERSONAL_ACCOUNT_TEXT))
        login.find_element(*Locators.LOGOUT_BUTTON).click()
        assert WebDriverWait(login, 3).until(expected_conditions.visibility_of_element_located(Locators.ENTER))
