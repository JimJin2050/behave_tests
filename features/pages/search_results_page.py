from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class SearchResultsPageLocator(object):
    # Search Results Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")


class SearchResultsPage(BasePage):
    # Search Results Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title

    def find_search_result(self, search_result):
        results = self.get_element(By.XPATH, "//a/em[contains(text(), '{}')]".format(search_result))
        return results
