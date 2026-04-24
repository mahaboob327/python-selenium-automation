from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")


@then("Verify message for 'Your cart is empty'")
def verify_empty_cart(context):
    actual = context.driver.find_element(*CART_EMPTY_MSG).text
    assert "Your cart is empty" in actual
    sleep(2)