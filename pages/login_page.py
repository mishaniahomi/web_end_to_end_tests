from .base_page import BasePage
from .locators import LoginPageLocators
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_input_username()
        self.should_be_input_password()
        self.go_to_profile_page()

    def should_be_input_username(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_USERNAME), (
            "Input for username is not presented"
        )

    def should_be_input_password(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_PASSWORD), (
            "Input for username is not presented"
        )

    def go_to_profile_page(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        print(f"Loading .env from: {dotenv_path}")
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        username = os.environ.get("LOGIN")
        password = os.environ.get("PASSWORD")
        username_input = self.browser.find_element(
            *LoginPageLocators.LOGIN_INPUT_USERNAME
        )
        username_input.send_keys(username)
        password_input = self.browser.find_element(
            *LoginPageLocators.LOGIN_INPUT_PASSWORD
        )
        password_input.send_keys(password)
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_link.click()
        WebDriverWait(self.browser, 10).until(EC.url_changes(self.browser.current_url))
        assert self.browser.current_url == os.environ.get("PROFILE_LINK"), f"Expected URL: {os.environ.get("PROFILE_LINK")}, but got: {self.browser.current_url}"
