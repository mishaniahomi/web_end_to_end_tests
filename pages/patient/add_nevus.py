from .photo_loader import PhotoLoader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from ..locators import PatientAddPhotoLocators


class AddNevus(PhotoLoader):
    """Class for testing patient/profile/{patient_id}/add/nevus"""

    def should_be_add_nevus(self):
        self.should_be_photo_loader()
        self.add_file("ISIC_0000002.jpg")
        
