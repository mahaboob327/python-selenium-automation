from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open Target main page")
def open_target_main(context):
    context.driver.get("https://www.target.com/")
    sleep(2)


@when("Click on the cart icon")
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
    sleep(5)


@when("Click Sign In button")
def click_sign_in(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/account']").click()
    sleep(3)


@when("Click Sign In from right side navigation menu")
def click_sign_in_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='login']").click()
    sleep(5)


@then("Verify message for 'Your cart is empty'")
def verify_empty_cart(context):
    actual = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert "Your cart is empty" in actual
    sleep(2)


@then("Verify Sign In form is displayed")
def verify_sign_in_form(context):
    actual = context.driver.find_element(By.CSS_SELECTOR, "input#username").is_displayed()
    assert actual, "Sign In form is not displayed"
    sleep(2)