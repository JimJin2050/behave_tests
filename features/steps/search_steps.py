# -*- coding: utf-8 -*-
from nose.tools import assert_equal, assert_true, assert_in

@Given('I navigate to the baidu Home page')
def step_impl(context):
    context.home_page.navigate("https://www.baidu.com")
    assert_equal(context.home_page.get_page_title(), u"百度一下，你就知道")

@When('I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search(search_term)


@Then('I am taken to the "{search_term}" Search Results page')
def step_impl(context, search_term):
    assert_in(search_term, context.search_results_page.get_page_title())

@Then('I see a search result "{search_result}"')
def step_impl(context, search_result):
    assert_true(context.search_results_page.find_search_result(search_result) is not None)
