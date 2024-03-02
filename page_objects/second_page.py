from selenium.webdriver.common.by import By

from page_objects.third_page import ThirPage  # it is written as an example


class SecondPage:
    def __init__(self, driver):
        self.driver = driver

    find_cities_by_zip_button = (By.LINK_TEXT, "Find Cities by ZIP")

    def click_on_find_cities_by_zip_button(self):
        button = self.driver.find_element(*SecondPage.find_cities_by_zip_button)
        button.click()
        assert "https://tools.usps.com/zip-code-lookup.htm?citybyzipcode" == self.driver.current_url
        third_page = ThirdPage(self.driver)  # it will activate the next page so you dont need to do it in actual test code
        return third_page