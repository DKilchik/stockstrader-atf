from pytest_bdd import then
from pages.home_page import HomePage


@then("home page should be opened")
def home_page_is_opened(browser):
    home_page = HomePage(browser)
    assert home_page.is_opened(), "The login page is not opened."
