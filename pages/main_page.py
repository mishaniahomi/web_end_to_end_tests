from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def should_be_main_page(self):
        self.is_main_page()

    def is_main_page(self):
        assert self.is_element_present(*MainPageLocators.IS_MAIN_PAGE), (
            "Main page is not presented"
        )
