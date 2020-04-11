from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        #self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 60)

    def wait_page_loaded(self):
        self.wait.until(PageLoaded())


class PageLoaded:
    def __call__(self, dr):
        ready = dr.execute_script(
                "return document.readyState=='complete';"
            )
        if ready:
            return True
        else:
            return False
