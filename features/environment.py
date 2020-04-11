#! python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
#from browser import Browser
from features.pages.home_page import HomePage
from features.pages.search_results_page import SearchResultsPage


def before_all(context):
    browser_type = context.config.userdata.get("browser", "chrome")
    headless = context.config.userdata.get("headless", "false").lower()
    if browser_type == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if headless == "true":
            firefox_options.add_argument("--headless")
        context.browser = webdriver.Firefox(
            executable_path='./geckodriver',
            options=firefox_options)
    elif browser_type == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if headless == "true":
            chrome_options.add_argument("--headless")
        context.browser = webdriver.Chrome(
            executable_path='./chromedriver',
            options=chrome_options)
    elif browser_type == "safari":
        context.browser = webdriver.Safari(
            executable_path='/usr/bin/safaridriver')
    else:
        context.browser = webdriver.Chrome()
    context.home_page = HomePage(context.browser)
    context.search_results_page = SearchResultsPage(context.browser)


def after_all(context):
    context.browser.close()


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    #print(feature.tags)
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass
