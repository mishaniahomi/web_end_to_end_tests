from .base import Patient
from ..locators import ListPersonalLocators


class ListPersonal(Patient):
    """Class for testing list of personal page (/patient/list/personal/)"""

    def should_be_list_personal(self):
        """function for running tests"""

        self.should_be_patient_id_input()
        self.should_be_search_button()
        self.should_be_patient_add_button()

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

    def should_be_patient_add_button(self):
        """Checking for the presence of patient add button"""

        assert self.is_element_present(*ListPersonalLocators.PATIENT_ADD_BUTTON), (
            "Patient add button is not presented"
        )

    def get_last_patient(self):
        """Function for getting last patient"""

        patient_list = self.browser.find_elements(
            *ListPersonalLocators.PATIENT_CARD_LINKS
        )
        assert len(patient_list) > 0, "patient list is empty"
        if patient_list:
            href = patient_list[-1].get_attribute("href")
            return href
    
    def go_to_last_patient(self):
        patient_list = self.browser.find_elements(
            *ListPersonalLocators.PATIENT_CARD_LINKS
        )
        assert len(patient_list) > 0, "patient list is empty"
        if patient_list:
            # self.click_to_element()
            patient_list[-1].click()
            # href = patient_list[-1].get_attribute("href")
            # return href
