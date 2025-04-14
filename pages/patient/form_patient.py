from .base import Patient
from ..locators import PatientFormLocator
from selenium.webdriver.support.ui import Select


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
        self.should_be_hair_type()
        self.should_be_nevus_places()
        self.should_be_nevus_count()
        self.should_be_immune()
        self.should_be_red_dots()
        self.should_be_group()
        self.should_be_sun_burn()
        self.should_be_nevus_size()
        self.should_be_comment()

    def should_be_hair_type(self):
        """Checking for the presence of a hair type select element"""

        assert self.is_element_present(*PatientFormLocator.HAIR_TYPE), (
            "hair type select is not presented"
        )

    def should_be_nevus_places(self):
        """Checking for the presence of a nevus places select element"""

        assert self.is_element_present(*PatientFormLocator.NEVUS_PLACES), (
            "nevus places select is not presented"
        )

    def should_be_nevus_count(self):
        """Checking for the presence of a nevus count select element"""

        assert self.is_element_present(*PatientFormLocator.NEVUS_COUNT), (
            "nevus count select is not presented"
        )

    def should_be_genetic(self):
        """Checking for the presence of a genetic select element"""

        assert self.is_element_present(*PatientFormLocator.GENETIC), (
            "genetic select is not presented"
        )

    def should_be_immune(self):
        """Checking for the presence of a immune select element"""

        assert self.is_element_present(*PatientFormLocator.RED_DOTS), (
            "immune select is not presented"
        )

    def should_be_red_dots(self):
        """Checking for the presence of a red dots select element"""

        assert self.is_element_present(*PatientFormLocator.RED_DOTS), (
            "red dots select is not presented"
        )

    def should_be_group(self):
        """Checking for the presence of a group select element"""

        assert self.is_element_present(*PatientFormLocator.GROUP), (
            "group select is not presented"
        )

    def should_be_sun_burn(self):
        """Checking for the presence of a sun burn select element"""

        assert self.is_element_present(*PatientFormLocator.SUN_BURN), (
            "sun burn select is not presented"
        )

    def should_be_nevus_size(self):
        """Checking for the presence of a nevus size select element"""

        assert self.is_element_present(*PatientFormLocator.NEVUS_SIZE), (
            "nevus size select is not presented"
        )

    def should_be_comment(self):
        """Checking for the presence of a comment input element"""

        assert self.is_element_present(*PatientFormLocator.COMMENT), (
            "More patient params show is not presented"
        )

    def basic_form_filling(self, age: int, sex: str):
        """_summary_

        Args:
            age (int): patient age > 1
            sex (str): patient sex allowed_values = {"man", "woman"}
        """
        self.age_filling(age=age)
        self.sex_select(sex=sex)

    def age_filling(self, age: int):
        """for filling patient age

        Args:
            age (int): patient age > 1
        """

        username_input = self.browser.find_element(*PatientFormLocator.AGE_INPUT)
        username_input.send_keys(age)

    def sex_select(self, sex: str):
        """for select sex

        Args:
            sex (str): patient sex allowed_values = {"man", "woman"}
        """

        select = Select(self.browser.find_element(*PatientFormLocator.SEX_SELECT))
        select.select_by_value(sex)
