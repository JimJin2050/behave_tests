from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Browser(object):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome() if you have set chromedriver in your PATH
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()
    wait = WebDriverWait(driver, 60)

    def close(context):
        context.driver.close()
