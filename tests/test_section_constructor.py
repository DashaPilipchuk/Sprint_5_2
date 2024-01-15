from locators import Locators
from const import Constants


class TestSectionConstructor:

    def test_go_to_section_sauces(self, driver):
        sauces = driver.find_element(*Locators.SAUCES)
        sauces.click()
        assert Constants.NEW_CLASS in sauces.get_attribute("class")

    def test_go_to_section_fillings(self, driver):
        fillings = driver.find_element(*Locators.FILLINGS)
        fillings.click()
        assert Constants.NEW_CLASS in fillings.get_attribute("class")

    def test_go_to_section_rolls(self, driver):
        fillings = driver.find_element(*Locators.FILLINGS)
        fillings.click()
        rolls = driver.find_element(*Locators.ROLLS)
        rolls.click()
        assert Constants.NEW_CLASS in rolls.get_attribute("class")


