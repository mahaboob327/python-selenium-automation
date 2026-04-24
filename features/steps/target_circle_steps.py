from selenium.webdriver.common.by import By
from behave import given, then, when
from time import sleep

STORY_CARDS = (By.CSS_SELECTOR, "div[data-test='storycardWrapperElement-div']")


@given("Open Target Circle page")
def open_circle_page(context):
    context.driver.get("https://www.target.com/circle")
    sleep(5)


@when("Circle page is loaded")
def wait_for_page(context):
    sleep(5)


@then("Verify 2 story cards are displayed under Unlock added value")
def verify_story_cards(context):
    cards = context.driver.find_elements(*STORY_CARDS)
    actual_count = len(cards)
    expected_count = 2

    assert actual_count == expected_count, f"Expected {expected_count} cards but got {actual_count}"
    sleep(2)