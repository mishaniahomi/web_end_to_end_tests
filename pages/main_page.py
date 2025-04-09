from .locators import MainPageLocators
from .other_page import OtherPage


class MainPage(OtherPage):
    def should_be_main_page(self):
        self.is_main_page()

    def is_main_page(self):
        assert self.is_element_present(*MainPageLocators.IS_MAIN_PAGE), (
            "Main page is not presented"
        )
