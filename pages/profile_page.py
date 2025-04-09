from .other_page import OtherPage
from .locators import ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class ProfilePage(OtherPage):
    def should_be_profile_page(self):
        self.should_be_link_to_main_page()


    def should_be_link_to_main_page(self):
        assert self.is_element_present(*ProfilePageLocators.MAIN_PAGE_LINK), (
            "Main page is not presented"
        )
    

    def go_to_patient_list_page(self): ...

    def go_to_patient_add_page(self): ...

    def go_to_patient_add_photo_page(self): ...

    def go_to_patient_add_hist_page(self): ...
    
    def go_to_main_page(self):
        link = self.browser.find_element(*ProfilePageLocators.MAIN_PAGE_LINK)
        link.click()
        WebDriverWait(self.browser, 100).until(EC.url_changes(self.browser.current_url))
        assert self.browser.current_url == os.environ.get("BASE_URL"), f"Expected URL: {os.environ.get("BASE_URL")}, but got: {self.browser.current_url}"
