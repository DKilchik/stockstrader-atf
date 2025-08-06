from .base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    SETTINGS_BLOCK = (By.CSS_SELECTOR, "#settings-block")

    def is_opened(self) -> bool:
        return self.element(self.SETTINGS_BLOCK, timeout=20, auto_search=False).is_present