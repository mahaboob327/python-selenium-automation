from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


@when("Click on the cart icon")
def click_cart(context,):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)


@when("Search for {search_query}")
def search_product(context, search_query):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_query)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(7)

