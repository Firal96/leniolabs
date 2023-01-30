import pytest
import json

from tests.pages.login import LoginPage

user_information = json.load(open('tests/fixtures/user_information.json'))

def test_succesful_login(browser):
    LoginPage(browser).load()
    user = user_information['standard_user']
    LoginPage(browser).fill_login(user['username'], user['password'])
    assert LoginPage(browser).get_title_label() == "PRODUCTS"
