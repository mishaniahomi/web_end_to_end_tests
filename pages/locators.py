from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    LOGIN_INPUT_USERNAME = (By.CSS_SELECTOR, "input#username")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "input#password")
    


class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    LOGIN_INPUT_USERNAME = (By.CSS_SELECTOR, "input#username")
