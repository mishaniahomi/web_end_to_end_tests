from .base import Patient
from ..locators import ListPersonalLocators


class ListPersonal(Patient):
    """Class for testing list of personal page (/patient/list/personal/)"""

    def should_be_list_personal(self):
        """function for running tests"""

        self.should_be_patient_id_input()
        self.should_be_search_button()

    def should_be_patient_id_input(self):
        """Checking for the presence of patient id input"""

        assert self.is_element_present(*ListPersonalLocators.PATIENT_ID), (
            "Patient input is not presented"
        )

    def should_be_search_button(self):
        """Checking for the presence of search button"""

        assert self.is_element_present(*ListPersonalLocators.SEARCH_BUTTON), (
            "Search button is not presented"
        )
