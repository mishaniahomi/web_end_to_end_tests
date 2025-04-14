from .base_page import BasePage
from .locators import LoginPageLocators
import os
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    """Class for testing login page"""

    def should_be_login_page(self) -> None:
        """Testing the login page"""

        self.should_be_input_username()
        self.should_be_input_password()
        self.should_be_login_button()
        # self.enter_wrong_credentials()
        self.go_to_profile_page()
       

    def should_be_login_button(self):
        """Checking for the presence of login button"""

        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), (
            "Login button is not presented"
        )

    def enter_credentials(self, username: str, password: str) -> None:
        """Function of entering login and password on the page

        Args:
            username (str): username
            password (str): password
        """

        username_input = self.browser.find_element(
            *LoginPageLocators.LOGIN_INPUT_USERNAME
        )
        username_input.send_keys(username)
        password_input = self.browser.find_element(
            *LoginPageLocators.LOGIN_INPUT_PASSWORD
        )
        password_input.send_keys(password)

    def should_be_input_username(self):
        """Checking for the presence of a username input element"""

        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_USERNAME), (
            "Input for username is not presented"
        )

    def should_be_input_password(self):
        """Checking for the presence of a username input element"""

        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_PASSWORD), (
            "Input for username is not presented"
        )
    
    def clear_username(self):
        self.clear_element(locator=LoginPageLocators.LOGIN_INPUT_USERNAME)
    
    def clear_password(self):
        self.clear_element(locator=LoginPageLocators.LOGIN_INPUT_PASSWORD)

    def enter_right_credentials(self):
        """Enter right credentials and click to login button"""

        username = os.environ.get("LOGIN")
        password = os.environ.get("PASSWORD")
        self.enter_credentials(username=username, password=password)
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)

    def enter_wrong_credentials(self):
        """Enter right credentials and click to login button"""

        self.enter_credentials(username="wrong_user", password="wrong_password")
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)
        self.clear_password()
        self.clear_username()

    def go_to_profile_page(self):
        """Check and go to profile page"""

        dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        self.enter_right_credentials()
        WebDriverWait(self.browser, 10).until(EC.url_changes(self.browser.current_url))
        assert self.browser.current_url == os.environ.get('BASE_URL')+os.environ.get("PROFILE_LINK"), (
            f"Expected URL: {os.environ.get('BASE_URL')+os.environ.get('PROFILE_LINK')}, but got: {self.browser.current_url}"
        )
