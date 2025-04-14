from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

class BasePage:
    """Base class for all page classes, which contains basic functions"""

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def click_to_element(self, locator):
        try:
            element = self.browser.find_element(*locator)
            element.click()
        except ElementNotInteractableException:
            return False
        return True


    def clear_element(self, locator):
        element = self.browser.find_element(*locator)    
        element.send_keys("")

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
