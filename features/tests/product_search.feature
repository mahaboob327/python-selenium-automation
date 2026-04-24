# Created by mahab at 4/19/2026
Feature: Test cases for Product Search on Target

  Scenario: User can search for a product "tea" on Target
    Given Open Target main page
    When Search for tea
    Then Verify search results for tea shown

  Scenario: User can search for a product "coffee" on Target
    Given Open Target main page
    When Search for coffee
    Then Verify search results for coffee shown


  Scenario: User can search for a product "coffee mug" on Target
    Given Open Target main page
    When Search for coffee mug
    Then Verify search results for coffee mug shown