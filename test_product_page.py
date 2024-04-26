import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import time
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "link",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail,
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    ],
)
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    result = page.click_on_add_cart_button()
    assert True == result, "Incorrect name or price of item"


# Ниже описаны отрицательные проверки.


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_cart_button()
    # You can write assert like this or how it was in  test_guest_cant_see_success_message function
    timeout = page.is_not_element_present(*ProductPageLocators.PRODUCT_TITLE)
    assert timeout == True, "Has message about adding a cart, expected False"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    # This variant of use is better than in upper function which is called
    # test_guest_cant_see_success_message_after_adding_product_to_basket
    assert page.is_not_element_present(
        *ProductPageLocators.ADDED_PRODUCT_TITLE
    ), "Success message is presented, but should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_cart_button()
    assert page.is_disappeared(
        *ProductPageLocators.ADDED_PRODUCT_TITLE
    ), "Wait until message will be deleted, but won't be"


# Еще тесты можно создавать в классах, нопосредственно в самих фвайлфх тестов
@pytest.mark.registration
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        email = str(time.time()) + "@fakemail.org"
        password = "123selenium"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    # doesn't work correctly
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(
            *ProductPageLocators.ADDED_PRODUCT_TITLE
        ), "Success message is presented, but should not be"

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.click_on_add_cart_button()
        assert False == page.is_disappeared(
            *ProductPageLocators.ADDED_PRODUCT_TITLE
        ), "Wait until message will be deleted, but won't be"
