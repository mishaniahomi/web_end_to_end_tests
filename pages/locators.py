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
    BURGER_OPEN = (
        By.XPATH,
        "//li[@class='dropdown dropdown-list-toggle']/a[@class='nav-link nav-link-lg sidebar-gone-show']",
    )  # это три полоски меню
    BURGER_CLOSE = (
        By.XPATH,
        "//div[@class='q-mini-drawer-hide absolute']/a[@class='nav-link nav-link-lg sidebar-gone-show']",
    )
    ASIDE = (By.XPATH, "//aside")
    CLOSE_ASIDE = (
        By.CSS_SELECTOR,
        "aside.q-drawer.q-drawer--left.q-drawer--bordered.q-layout--prevent-focus.q-drawer--standard.fixed.q-drawer--on-top",
    )
    OPEN_ASIDE = (
        By.CSS_SELECTOR,
        "aside.q-drawer.q-drawer--left.q-drawer--bordered.q-drawer--standard.fixed.q-drawer--on-top",
    )


class PatientFormLocator:
    AGE_INPUT = (By.CSS_SELECTOR, "#age")
    SEX_SELECT = (By.CSS_SELECTOR, "#sex")
    ACCORDION = (By.CSS_SELECTOR, "#accordion")
    SHOW_MORE_PATIENT_PARAMS = (
        By.XPATH,
        "//div[@class='accordion-body collapse show' and @id='more_patient_params']",
    )
    HAIR_TYPE = (By.CSS_SELECTOR, "#hair_type")
    SKIN = (By.CSS_SELECTOR, "#skin")
    NEVUS_PLACES = (By.CSS_SELECTOR, "#nevus_places")
    NEVUS_COUNT = (By.CSS_SELECTOR, "#nevus_count")
    GENETIC = (By.CSS_SELECTOR, "#genetic")
    IMMUNE = (By.CSS_SELECTOR, "#immune")
    RED_DOTS = (By.CSS_SELECTOR, "#red_dots")
    GROUP = (By.CSS_SELECTOR, "#group")
    SUN_BURN = (By.CSS_SELECTOR, "#sun_burn")
    NEVUS_SIZE = (By.CSS_SELECTOR, "#nevus_size")
    COMMENT = (By.CSS_SELECTOR, "#comment")


class PatientAddPageLocator:
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_button")


class PatientPageLocators: ...
