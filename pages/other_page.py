from .base_page import BasePage
from .locators import OtherPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class OtherPage(BasePage):
    def should_be_other_page(self):
        self.should_be_aside()
        self.should_be_link_to_patient_list()
        self.should_be_link_to_patient_add()
        self.should_be_link_to_patient_add_photo()
        self.should_be_burger_open()
        self.should_be_dropdown()
        self.should_be_open_dropdown()

        # self.go_to_patient_list_page()
        # self.go_to_patient_add_page()
        # self.go_to_patient_add_photo_page()
        # self.go_to_patient_add_hist_page()

    def should_be_open_dropdown(self):
        """Checking for the presence of dropdown when open"""

        self.click_to_element(OtherPageLocators.DROPDOWN)
        assert self.is_element_present(*OtherPageLocators.DROPDOWN_SHOW), (
            "dropdown show is not presented"
        )
    
    

    def should_be_dropdown(self):
        """Checking for the presence of dropdown"""

        assert self.is_element_present(*OtherPageLocators.DROPDOWN), (
            "dropdown is not presented"
        )

    def should_be_burger_open(self):
        """Checking for the presence of burger when open"""
        assert self.is_element_present(*OtherPageLocators.BURGER_OPEN), (
            "BURGER_OPEN is not presented"
        )

    def should_be_aside(self):
        assert self.is_element_present(*OtherPageLocators.ASIDE), (
            "ASIDE is not presented"
        )

    def should_be_link_to_patient_list(self):
        assert self.is_element_present(*OtherPageLocators.PATIENT_LIST), (
            "Link to patient list is not presented"
        )

    def should_be_link_to_patient_add(self):
        assert self.is_element_present(*OtherPageLocators.PATIENT_ADD), (
            "Link to adding patient is not presented"
        )

    def should_be_link_to_patient_add_photo(self):
        assert self.is_element_present(*OtherPageLocators.PATIENT_ADD_PHOTO), (
            "Link to adding photo is not presented"
        )

    def should_be_link_to_patient_add_histo(self):
        assert self.is_element_present(*OtherPageLocators.PATIENT_ADD_HISTO), (
            "Link to adding histo is not presented"
        )

    def go_to_patient_list_page(self):
        self.click_to_element(OtherPageLocators.BURGER_OPEN)
        self.click_to_element(OtherPageLocators.PATIENT_LIST)
        WebDriverWait(self.browser, 10).until(EC.url_changes(self.browser.current_url))
        assert self.browser.current_url == os.environ.get("BASE_URL") + os.environ.get(
            "PATIENT_LINK"
        ), (
            f"Expected URL: {os.environ.get('BASE_URL') + os.environ.get('PATIENT_LINK')}, but got: {self.browser.current_url}"
        )

    def go_to_patient_add_page(self):
        self.click_to_element(OtherPageLocators.BURGER_OPEN)
        self.click_to_element(OtherPageLocators.PATIENT_ADD)
        WebDriverWait(self.browser, 10).until(EC.url_changes(self.browser.current_url))
        assert self.browser.current_url == os.environ.get("BASE_URL") + os.environ.get(
            "PATIENT_ADD_LINK"
        ), (
            f"Expected URL: {os.environ.get('BASE_URL') + os.environ.get('PATIENT_ADD_LINK')}, but got: {self.browser.current_url}"
        )

    def go_to_patient_add_photo_page(self):
        self.click_to_element(OtherPageLocators.BURGER_OPEN)
        self.click_to_element(OtherPageLocators.PATIENT_ADD_PHOTO)
        WebDriverWait(self.browser, 10).until(EC.url_changes(self.browser.current_url))
        assert self.browser.current_url == os.environ.get("BASE_URL") + os.environ.get(
            "PATIENT_ADD_PHOTO_LINK"
        ), (
            f"Expected URL: {os.environ.get('BASE_URL') + os.environ.get('PATIENT_ADD_PHOTO_LINK')}, but got: {self.browser.current_url}"
        )

    def go_to_patient_add_hist_page(self):
        self.click_to_element(OtherPageLocators.BURGER_OPEN)
        self.click_to_element(OtherPageLocators.PATIENT_ADD_HISTO)
        WebDriverWait(self.browser, 10).until(EC.url_changes(self.browser.current_url))
        assert self.browser.current_url == os.environ.get("BASE_URL") + os.environ.get(
            "PATIENT_ADD_HISTO_LINK"
        ), (
            f"Expected URL: {os.environ.get('BASE_URL') + os.environ.get('PATIENT_ADD_HISTO_LINK')}, but got: {self.browser.current_url}"
        )
