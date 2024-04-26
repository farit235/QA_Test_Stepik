from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, type_of_search, what_to_search):
        try:
            self.browser.find_element(type_of_search, what_to_search)
        except NoSuchElementException:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), (
            "User icon is not presented," " probably unauthorised user"
        )
