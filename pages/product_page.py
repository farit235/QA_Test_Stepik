import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


def get_name(self, find_by, what):
    name = self.browser.find_element(find_by, what).text
    return name


def get_price(self, find_by, what):
    price = self.browser.find_element(find_by, what).text
    return price


def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
    return answer


class ProductPage(BasePage):
    def click_on_add_cart_button(self):
        to_cart_button = self.browser.find_element(*ProductPageLocators.TO_CART_BUTTON)
        to_cart_button.click()
        solve_quiz_and_get_code(self)
        name = get_name(self, *ProductPageLocators.ADDED_PRODUCT_TITLE)
        # price = get_price(self, *ProductPageLocators.ADDED_PRODUCT_PRICE)
        if name == self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text:
            return True
        else:
            return False


