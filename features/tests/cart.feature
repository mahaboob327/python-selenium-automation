# Created by mahab at 4/21/2026
Feature: Cart test cases

  Scenario: User can open cart and see empty message
    Given Open Target main page
    When Click on the cart icon
    Then Verify "Your cart is empty" message is displayed


  Scenario: User can add product to cart and verify it
    Given Open Target main page
    When Search for mug
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify correct product is in cart