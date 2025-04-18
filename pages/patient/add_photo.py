from ..locators import PatientAddPhotoLocators
from .photo_loader import PhotoLoader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class AddPhoto(PhotoLoader):
    def should_be_add_photo_page(self):
        self.should_be_photo_loader()
        self.should_be_patient_id_input()
        self.add_photo()

    def should_be_patient_id_input(self):
        """Checking for the presence of patient id input"""

        assert self.is_element_present(*PatientAddPhotoLocators.PATIENT_ID), (
            "Patient input is not presented"
        )

    def add_photo(self):
        patient_id_input = self.browser.find_element(
            *PatientAddPhotoLocators.PATIENT_ID
        )
        patient_id_input.send_keys("157")
        self.load_file()
        comment_input = self.browser.find_element(*PatientAddPhotoLocators.COMMENT)
        comment_input.send_keys("test")
        self.click_to_element(locator=PatientAddPhotoLocators.ADD_BUTTON)
        WebDriverWait(self.browser, 10).until(EC.url_changes(self.browser.current_url))
        assert "/patient/profile/157" in self.browser.current_url, (
            f"Expected URL: {os.environ.get('BASE_URL') + "/patient/profile/157"}, but got: {self.browser.current_url}"
        )
        
