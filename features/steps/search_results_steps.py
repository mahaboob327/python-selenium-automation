from itertools import product

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_COUNT_TEXT = (By.XPATH, "//div[contains(@class, 'styles_resultCount')]")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(2)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(2)


@then("Verify search results for {product} shown")
def verify_search_results(context, product):
    actual_result = context.driver.find_element(*SEARCH_RESULTS_COUNT_TEXT).text
    assert product in actual_result, f'Expected "{product}" not in actual "{actual_result}"'
