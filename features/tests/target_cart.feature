Feature: Target cart and sign-in functionality

  Scenario: User can open cart and see empty message
    Given Open Target main page
    When Click on the cart icon
    Then Verify "Your cart is empty" message is displayed

  Scenario: Logged out user can navigate to Sign In page
    Given Open Target main page
    When Click Sign In button
    And Click Sign In from right side navigation menu
    Then Verify Sign In form is displayed