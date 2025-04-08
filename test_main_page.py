from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
import time


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def setup_browser(func):
    def wrapper():
        cService = webdriver.ChromeService(
            executable_path=ChromeDriverManager().install()
        )
        browser = webdriver.Chrome(service=cService)
        try:
            func(browser)
        finally:
            browser.quit()

    return wrapper


@setup_browser
def test_guest_login_page(browser):
    base_url = os.environ.get("BASE_URL")
    link = base_url + "login"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()


@setup_browser
def test_quest_main_page(browser):
    base_url = os.environ.get("BASE_URL")
    link = base_url + "login"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.go_to_profile_page()
    profile_page = ProfilePage(browser, browser.current_url)
    profile_page.go_to_main_page()
    main_page = MainPage(browser, browser.current_url)
    main_page.should_be_main_page()


@setup_browser
def test_quest_profile_page(browser):
    base_url = os.environ.get("BASE_URL")
    link = base_url + "login"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.go_to_profile_page()
    profile_page = ProfilePage(browser, browser.current_url)
    profile_page.should_be_profile_page()
