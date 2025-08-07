from pytest_bdd import given, when, then,  parsers
from pages.login_page import LoginPage
from data.test_data import get_conf_param

@given("user opens the login page")
def open_login_page(browser):
    page = LoginPage(browser)
    page.open()

@when("user enter valid username")
def enter_valid_username(browser):
    page = LoginPage(browser)
    page.enter_username(get_conf_param("ACCOUNT", "username"))

@when(parsers.parse("user enter '{username}' username"))
def enter_username(browser, username):
    page = LoginPage(browser)
    page.enter_username(username)

@when("user enter valid password")
def enter_valid_password(browser):
    page = LoginPage(browser)
    page.enter_password(get_conf_param("ACCOUNT", "password"))

@when(parsers.parse("user enter '{password}' password"))
def enter_password(browser, password):
    page = LoginPage(browser)
    page.enter_password(password)

@when("user click continue button")
def click_continue(browser):
    page = LoginPage(browser)
    page.click_continue()

@then("invalid credentials label should be present")
def click_continue(browser):
    page = LoginPage(browser)
    assert page.is_invalid_creds_label_present(), "Invalid credentials label is missing"
