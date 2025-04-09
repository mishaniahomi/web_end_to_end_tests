from .base_page import BasePage
from .locators import OtherPageLocators


class OtherPage(BasePage):
    def should_be_other_page(self):
        self.should_be_aside()

    def should_be_aside(self):
        assert self.is_element_present(*OtherPageLocators.ASIDE), (
            "ASIDE is not presented"
        )

    def go_to_patient_list_page(self): ...

    def go_to_patient_add_page(self): ...

    def go_to_patient_add_photo_page(self): ...

    def go_to_patient_add_hist_page(self): ...
