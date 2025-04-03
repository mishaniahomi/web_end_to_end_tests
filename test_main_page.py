from pages.main_page import MainPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def test_guest_can_go_to_login_page():
    link = "https://dev-cab.dev-ai-melanoma.ru/login"
    cService = webdriver.ChromeService(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service = cService)
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

