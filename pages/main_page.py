from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
        login_link.click()

    def should_be_input_username(self):
        assert self.is_element_present(By.CSS_SELECTOR, "input#username"), "Input for username is not presented"
