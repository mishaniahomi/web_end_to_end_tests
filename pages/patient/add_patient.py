from .form_patient import FormPatient
from ..locators import PatientAddPageLocator
import time

class AddPatient(FormPatient):
    def should_be_add_patient_page(self):
        self.should_be_add_button()
        self.should_be_form_patient()


    def should_be_add_button(self):
        """Checking for the presence of a add button element"""

        assert self.is_element_present(*PatientAddPageLocator.ADD_BUTTON), (
            "Add button is not presented"
        )


