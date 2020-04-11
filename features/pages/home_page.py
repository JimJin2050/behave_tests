from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
#from browser import Browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class HomePageLocator(object):
    # Home Page Locators

    SEARCH_FIELD = (By.ID, "kw")


class HomePage(BasePage):
    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.fill(Keys.ENTER, *HomePageLocator.SEARCH_FIELD)
        self.wait_page_loaded()
        self.wait.until(EC.title_contains(search_term))
