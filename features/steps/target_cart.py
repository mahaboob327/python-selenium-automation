from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    sleep(2)


@when("Click on the cart icon")
def click_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(10)


@then('Verify message for Your cart is empty')
def verify_empty_cart(context):
    context.driver.find_element(By.XPATH, "//*[contains(text(),'Your cart is empty')]")