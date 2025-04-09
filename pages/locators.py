from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    LOGIN_INPUT_USERNAME = (By.CSS_SELECTOR, "input#username")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "input#password")


class MainPageLocators:
    IS_MAIN_PAGE = (By.XPATH, "//h1[text()='Главная страница']")


class ProfilePageLocators:
    MAIN_PAGE_LINK = (By.XPATH, "//a[@href='/' and text()='Главная страница']")


class OtherPageLocators:
    PATIENT_LIST = (By.XPATH, "//a[@href='/patient/list/personal/']")
    BURGER = (By.XPATH, "//a[@data-toggle='sidebar'']")  # это три полоски меню
    ASIDE = (By.XPATH, "//aside")
    CLOSE_ASIDE = (
        By.CSS_SELECTOR,
        "aside.q-drawer.q-drawer--left.q-drawer--bordered.q-layout--prevent-focus.q-drawer--standard.fixed.q-drawer--on-top",
    )
    OPEN_ASIDE = (
        By.CSS_SELECTOR,
        "aside.q-drawer.q-drawer--left.q-drawer--bordered.q-drawer--standard.fixed.q-drawer--on-top",
    )

class PatientPageLocators: ...
    
