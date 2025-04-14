from .base import Patient
from ..locators import PatientFormLocator


class FormPatient(Patient):
    """Class for testing patient form"""

    def should_be_form_patient(self):
        self.should_be_age_input()
        self.should_be_sex_select()
        self.should_be_accordion()
        self.should_be_more_patient_params_show()

    def should_be_age_input(self):
        """Checking for the presence of a age input element"""

        assert self.is_element_present(*PatientFormLocator.AGE_INPUT), (
            "Input for age is not presented"
        )

    def should_be_sex_select(self):
        """Checking for the presence of a sex select element"""

        assert self.is_element_present(*PatientFormLocator.AGE_INPUT), (
            "Select for sex is not presented"
        )

    def should_be_accordion(self):
        """Checking for the presence of a accordion element"""

        assert self.is_element_present(*PatientFormLocator.ACCORDION), (
            "Accordion is not presented"
        )

    def should_be_more_patient_params_show(self):
        """Checking for the presence of a more patient params"""
        self.click_to_element(PatientFormLocator.ACCORDION)

        assert self.is_element_present(*PatientFormLocator.SHOW_MORE_PATIENT_PARAMS), (
            "More patient params show is not presented"
        )
        self.should_be_comment()

    def should_be_comment(self):
        """Checking for the presence of a comment input element"""

        assert self.is_element_present(*PatientFormLocator.COMMENT), (
            "More patient params show is not presented"
        )
