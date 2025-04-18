from .base import Patient
from ..locators import PhotoLoaderLocator
import os
import time


class PhotoLoader(Patient):
    """Class for testing load of photo"""

    def should_be_photo_loader(self):
        self.should_be_histo_selector()
        self.should_be_diagnosis_selector()
        self.should_be_photo_loader_input()
        self.should_be_comment()
        self.should_be_add_button()

    def should_be_histo_selector(self):
        """Checking for the presence of histo selector (да/нет)"""

        assert self.is_element_present(*PhotoLoaderLocator.HISTO_ID), (
            "Histo selector (да/нет) is not presented"
        )

    def should_be_diagnosis_selector(self):
        """Checking for the presence of diagnosis selector"""

        assert self.is_element_present(*PhotoLoaderLocator.DIAGNOSIS_ID), (
            "Diagnosis selector is not presented"
        )

    def should_be_photo_loader_input(self):
        """Checking for the presence of photo loader"""

        assert self.is_element_present(*PhotoLoaderLocator.PHOTO_LOADER), (
            "Photo loader is not presented"
        )

    def should_be_comment(self):
        """Checking for the presence of comment"""

        assert self.is_element_present(*PhotoLoaderLocator.COMMENT), (
            "Comment is not presented"
        )

    def should_be_add_button(self):
        """Checking for the presence of a add button element"""

        assert self.is_element_present(*PhotoLoaderLocator.ADD_BUTTON), (
            "Add button is not presented"
        )

    def load_file(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        test_images_dir = os.path.abspath(
            os.path.join(current_dir, "../../test_images/")
        )
        file_path = os.path.join(test_images_dir, "ISIC_0000002.jpg")
        element = self.browser.find_element(*PhotoLoaderLocator.PHOTO_LOADER)
        element.send_keys(file_path)
        time.sleep(5)
