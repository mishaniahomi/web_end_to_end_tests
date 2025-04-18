from ..locators import PatientAddPhotoLocators
from .photo_loader import PhotoLoader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class AddPhoto(PhotoLoader):
    def should_be_add_photo_page(self):
        self.should_be_photo_loader()
        self.should_be_patient_id_input()
        self.add_photo("ISIC_0000002.jpg")

    def should_be_patient_id_input(self):
        """Checking for the presence of patient id input"""

        assert self.is_element_present(*PatientAddPhotoLocators.PATIENT_ID), (
            "Patient input is not presented"
        )

    def add_photo(self, image_name):
        patient_id_input = self.browser.find_element(
            *PatientAddPhotoLocators.PATIENT_ID
        )
        patient_id_input.send_keys("157")
        self.add_file(image_name)
