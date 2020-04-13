# coding:utf-8
__author__ = 'Jim'

import requests
from requests import HTTPError
from behave import *

@Given('request type is {request_type}')
def step_impl(context, request_type):
    context.request_type = request_type

@When('I input HTTP api {url} and {parameters}')
def step_impl(context, url, parameters):
    context.url = url
    context.parameters = parameters

@Then('The status code is 200')
def step_impl(context):
    try:
        if context.request_type == 'get':
            res = requests.get(url=context.url, params=context.parameters)
        elif context.request_type == 'post':
            res = requests.post(url=context.url, data=context.parameters)
        assert res.status_code == 200
    except HTTPError as e:
        print(e.strerror)
        print(e.args)
