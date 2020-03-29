from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from features.browser import Browser
#from browser import Browser
from features.pages.home_page import HomePage
from features.pages.search_results_page import SearchResultsPage



def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()


def after_all(context):
    context.browser.close()


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    print(feature.tags)
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
