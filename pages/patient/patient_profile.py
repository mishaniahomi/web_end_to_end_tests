from .form_patient import FormPatient
from ..locators import PatientProfileLocators
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PatientProfile(FormPatient):
    """Class for testing of patient profile"""

    def should_be_patient_profile(self):
        self.should_be_form_patient()
        self.should_be_save_button()
        self.should_be_get_report_button()
        self.should_be_nevus_add_button()
        self.go_to_add_nevus()

    def should_be_delete_button(self):
        """Checking for the presence of delete button"""

        self.should_be_more_patient_params_show()

        assert self.is_element_present(*PatientProfileLocators.DELETE_BUTTON), (
            "Delete button is not presented"
        )

    def should_be_save_button(self):
        """Checking for the presence of save button"""

        assert self.is_element_present(*PatientProfileLocators.SAVE_BUTTON), (
            "Save button is not presented"
        )

    def should_be_get_report_button(self):
        """Checking for the presence of get report button"""

        assert self.is_element_present(*PatientProfileLocators.GET_REPORT_BUTTON), (
            "Get report button is not presented"
        )

    def should_be_nevus_add_button(self):
        """Checking for the presence of nevus add button"""

        assert self.is_element_present(*PatientProfileLocators.NEVUS_ADD_BUTTON), (
            "Nevus add button is not presented"
        )

    def go_to_add_nevus(self):
        """Function for go to nevus add page"""

        self.click_to_element(PatientProfileLocators.NEVUS_ADD_BUTTON)
        WebDriverWait(self.browser, 10).until(EC.url_changes(self.browser.current_url))
        assert (
            os.environ.get("BASE_URL") + "patient/profile/157/add/nevus"
            in self.browser.current_url
        ), (
            f"Expected URL: {os.environ.get('BASE_URL') + os.environ.get('PATIENT_PROFILE')}/id, but got: {self.browser.current_url}"
        )

    def delete_patient(self):
        """For deleting of patient"""

        self.should_be_more_patient_params_show()
        self.click_to_element(PatientProfileLocators.DELETE_BUTTON)


