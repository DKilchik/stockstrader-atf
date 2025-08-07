from selenium.webdriver.common.by import By
from utils import Configuration
from .base_page import BasePage


class LoginPage(BasePage):
    URL = Configuration.BASE_PAGE + "/login"

    USERNAME_FIELD = (By.XPATH, "//input[@type='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    CONTINUE_SHADOW_HOST = (By.CSS_SELECTOR, "div.login-action ion-button[type='button']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button.button-native")
    INVALID_CREDENTIAL_LABEL = (By.XPATH, "//ion-label[text()='Invalid credentials']")

    def open(self):
        self._browser.get(self.URL)

    def enter_username(self, username):
        self.element(self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.element(self.PASSWORD_FIELD).send_keys(password)

    def click_continue(self):
        self.element(self.CONTINUE_SHADOW_HOST).shadow_child(self.CONTINUE_BUTTON).click(js=True)

    def is_invalid_creds_label_present(self) -> bool:
        return self.element(self.INVALID_CREDENTIAL_LABEL, timeout=10, auto_search=False).is_present
