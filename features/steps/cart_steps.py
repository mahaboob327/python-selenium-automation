from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
TOTAL_TXT = (By.XPATH, "//h2[./span[contains(text(), 'subtotal')]]")



@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"

@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart(context):
    actual = context.driver.find_element(*CART_EMPTY_MSG).text
    assert "Your cart is empty" in actual
    sleep(2)