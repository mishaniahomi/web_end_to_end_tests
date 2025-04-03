from pages.main_page import MainPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def test_guest_can_go_to_login_page():
    cService = webdriver.ChromeService(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=cService)
    base_url = os.environ.get("BASE_URL")
    link = base_url + "/login"
    page = MainPage(
        browser, link
    )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина


def test_quest_should_be_input_username():
    cService = webdriver.ChromeService(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=cService)
    base_url = os.environ.get("BASE_URL")
    link = base_url + "/login"
    page = MainPage(
        browser, link
    )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_input_username()  # выполняем метод страницы — переходим на страницу логина
