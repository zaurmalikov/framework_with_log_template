from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.second_page import SecondPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    quick_tools_menu = (By.XPATH, "//a[@class='nav-first-element menuitem']")
    all_quick_tools_menu_items = (By.XPATH, "//li[@class='qt-nav menuheader']/div/ul/li")

    def perform_some_action(self):
        action = ActionChains(self.driver)
        move = action.move_to_element(self.driver.find_element(*MainPage.quick_tools_menu)).perform()
        return move

    def perform_following_action(self):
        menu_items = self.driver.find_elements(*MainPage.all_quick_tools_menu_items)
        for item in menu_items:
            if "Look Up a" in item.text:
                item.click()
                break
        assert "ZIP Code™ Lookup | USPS" in self.driver.title
        second_page = SecondPage(self.driver)  # it will activate the next page so you dont need to do it in actual test code
        return second_page