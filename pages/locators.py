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
    PATIENT_ADD = (By.XPATH, "//a[@href='/patient/add/']")
    PATIENT_ADD_PHOTO = (By.XPATH, "//a[@href='/patient/add/photo/']")
    PATIENT_ADD_HISTO = (By.XPATH, "//a[@href='/patient/add/histo/']")
    BURGER_OPEN = (By.XPATH, "//li[@class='dropdown dropdown-list-toggle']/a[@class='nav-link nav-link-lg sidebar-gone-show']")  # это три полоски меню
    BURGER_CLOSE = (By.XPATH, "//div[@class='q-mini-drawer-hide absolute']/a[@class='nav-link nav-link-lg sidebar-gone-show']")
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
    
