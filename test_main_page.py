from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.patient.add_patient import AddPatient
from pages.patient.add_photo import AddPhoto
from pages.patient.list_personal import ListPersonal
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
        browser.implicitly_wait(os.environ.get("IMPLICITLY_WAIT"))
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
def test_quest_other_page(browser):
    base_url = os.environ.get("BASE_URL")
    link = base_url + "login"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.go_to_profile_page()
    profile_page = ProfilePage(browser, browser.current_url)
    profile_page.should_be_other_page()


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

@setup_browser
def test_quest_patient_list_page(browser):
    base_url = os.environ.get("BASE_URL")
    link = base_url + "login"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.go_to_profile_page()
    profile_page = ProfilePage(browser, browser.current_url)
    profile_page.go_to_patient_list_page()
    patient_add_page = ListPersonal(browser, browser.current_url)
    patient_add_page.should_be_list_personal()

@setup_browser
def test_quest_patient_add_page(browser):
    base_url = os.environ.get("BASE_URL")
    link = base_url + "login"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.go_to_profile_page()
    profile_page = ProfilePage(browser, browser.current_url)
    profile_page.go_to_patient_add_page()
    patient_add_page = AddPatient(browser, browser.current_url)
    patient_add_page.should_be_add_patient_page()


@setup_browser
def test_quest_patient_photo_add_page(browser):
    base_url = os.environ.get("BASE_URL")
    link = base_url + "login"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.go_to_profile_page()
    profile_page = ProfilePage(browser, browser.current_url)
    profile_page.go_to_patient_add_photo_page()
    patient_add_page = AddPhoto(browser, browser.current_url)
    patient_add_page.should_be_add_photo_page() #TODO: Тут доделать надо, чтобы ошибку давало

