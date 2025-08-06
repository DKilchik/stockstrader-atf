from pytest_bdd import given, when
from pages.login_page import LoginPage
from data.test_data import get_conf_param

@given("user opens the login page")
def open_login_page(browser):
    page = LoginPage(browser)
    page.open()

@when("user enter valid username")
def enter_username(browser):
    page = LoginPage(browser)
    page.enter_username(get_conf_param("ACCOUNT", "username"))

@when("user enter valid password")
def enter_password(browser):
    page = LoginPage(browser)
    page.enter_password(get_conf_param("ACCOUNT", "password"))

@when("user click continue button")
def click_continue(browser):
    page = LoginPage(browser)
    page.click_continue()