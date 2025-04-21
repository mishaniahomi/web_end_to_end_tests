from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    LOGIN_INPUT_USERNAME = (By.CSS_SELECTOR, "input#username")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "input#password")


class MainPageLocators:
    IS_MAIN_PAGE = (By.XPATH, "//h1[text()='Главная страница']")


class ProfilePageLocators:
    MAIN_PAGE_LINK = (By.XPATH, "//a[@href='/' and text()='Главная страница']")
    INPUT_USERNAME = (By.CSS_SELECTOR, "input#username")
    INPUT_SURNAME = (By.CSS_SELECTOR, "input#surname")
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "input#firstname")
    INPUT_PATRONYMIC = (By.CSS_SELECTOR, "input#patronymic")
    INPUT_WORK_PLACE = (By.CSS_SELECTOR, "input#work_place")
    INPUT_JOB_TITLE = (By.CSS_SELECTOR, "input#job_title")
    INPUT_LS_API_KEY = (By.CSS_SELECTOR, "input#ls_api_key")
    INPUT_ROLE = (By.CSS_SELECTOR, "input#role")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button#delete_button")
    PASSWORD_BUTTON = (By.CSS_SELECTOR, "button#password_button")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button#save_button")


class OtherPageLocators:
    PATIENT_LIST = (By.XPATH, "//a[@href='/patient/list/personal/']")
    PATIENT_ADD = (By.XPATH, "//a[@href='/patient/add/']")
    PATIENT_ADD_PHOTO = (By.XPATH, "//a[@href='/patient/add/photo/']")
    PATIENT_ADD_HISTO = (By.XPATH, "//a[@href='/patient/add/histo/']")
    BURGER_OPEN = (
        By.XPATH,
        "//li[@class='dropdown dropdown-list-toggle']/a[@class='nav-link nav-link-lg sidebar-gone-show']",
    )
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
    DROPDOWN = (
        By.XPATH,
        "/html/body/div[1]/div/nav/ul[2]/li[@class='dropdown']",
    )
    DROPDOWN_SHOW = (
        By.XPATH,
        "/html/body/div[1]/div/nav/ul[2]/li[@class='dropdown show']",
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


class PatientAddPhotoLocators:
    PATIENT_ID = (By.CSS_SELECTOR, "#patient_id")
    HISTO_ID = (By.CSS_SELECTOR, "#histo")
    DIAGNOSIS_ID = (By.CSS_SELECTOR, "#diagnosis")
    PHOTO_LOADER = (By.CSS_SELECTOR, "#photo_loader")
    COMMENT = (By.CSS_SELECTOR, "#comment")
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_button")


class PhotoLoaderLocator:
    HISTO_ID = (By.CSS_SELECTOR, "#histo")
    DIAGNOSIS_ID = (By.CSS_SELECTOR, "#diagnosis")
    PHOTO_LOADER = (By.CSS_SELECTOR, "#photo_loader")
    COMMENT = (By.CSS_SELECTOR, "#comment")
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_button")


class ListPersonalLocators:
    PATIENT_ID = (By.CSS_SELECTOR, "#patient_id")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary.form-control")
    PATIENT_ADD_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-success.form-control")
    PATIENT_CARD_LINKS = (By.XPATH, "//a[@class='card-link'and text()=' Подробно... ']")


class PatientProfileLocators:
    SAVE_BUTTON = (By.CSS_SELECTOR, "#save_button")
    GET_REPORT_BUTTON = (By.CSS_SELECTOR, "#get_report_button")
    NEVUS_ADD_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-success.form-control")
    DELETE_BUTTON = (By.CSS_SELECTOR, "#delete_button")
