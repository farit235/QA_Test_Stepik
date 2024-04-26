from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_FIELD_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_FIELD_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_FIELD_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    APPLY_REGISTRATION_FORM_BUTTON = (
        By.CSS_SELECTOR,
        "#register_form > button:nth-child(7)",
    )
    SUCCESSFUL_REGISTRATION_MESSAGE = (By.CLASS_NAME, ".alertinner")


class ProductPageLocators:
    TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn:nth-child(3)")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    PRODUCT_PRICE = (By.CLASS_NAME, ".price_color")
    ADDED_PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        "#messages > div:nth-child(1) > div > strong",
    )
    ADDED_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong",
    )
