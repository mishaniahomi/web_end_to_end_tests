from .form_patient import FormPatient
from ..locators import PatientAddPageLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import random


class AddPatient(FormPatient):
    """"""

    def should_be_add_patient_page(self):
        """_summary_"""
        self.should_be_add_button()
        self.should_be_form_patient()
        self.add_patient()

    def should_be_add_button(self):
        """Checking for the presence of a add button element"""

        assert self.is_element_present(*PatientAddPageLocator.ADD_BUTTON), (
            "Add button is not presented"
        )

    def add_patient(self):
        """Function for auto adding of patient"""

        self.basic_form_filling(age=random.randint(1, 149), sex="man")
        self.click_to_element(PatientAddPageLocator.ADD_BUTTON)
        WebDriverWait(self.browser, 10).until(EC.url_changes(self.browser.current_url))
        assert (
            os.environ.get("BASE_URL") + os.environ.get("PATIENT_PROFILE")
            in self.browser.current_url
        ), (
            f"Expected URL: {os.environ.get('BASE_URL') + os.environ.get('PATIENT_PROFILE')}/id, but got: {self.browser.current_url}"
        )
