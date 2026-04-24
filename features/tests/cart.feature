# Created by mahab at 4/21/2026
Feature: Cart test cases

  Scenario: User can open cart and see empty message
    Given Open Target main page
    When Click on the cart icon
    Then Verify "Your cart is empty" message is displayed