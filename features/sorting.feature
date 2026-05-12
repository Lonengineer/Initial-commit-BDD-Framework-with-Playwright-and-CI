Feature: Product Sorting
  As a logged-in user
  I want to sort products by different criteria
  So that I can find products more easily

  Background:
    Given the user is logged in and on the products page

  # Test Case 1: Verify products can be sorted from A-Z
  Scenario: Sort products by name from A to Z
    When the user selects "Name (A to Z)" from the sort dropdown
    Then the products should be sorted alphabetically from A to Z

  # Test Case 2: Verify products can be sorted from Z-A
  Scenario: Sort products by name from Z to A
    When the user selects "Name (Z to A)" from the sort dropdown
    Then the products should be sorted alphabetically from Z to A

  # Test Case 3: Verify products can be sorted by low-to-high price
  Scenario: Sort products by price from low to high
    When the user selects "Price (low to high)" from the sort dropdown
    Then the products should be sorted by price from low to high

  # Test Case 4: Verify products can be sorted by high-to-low price
  Scenario: Sort products by price from high to low
    When the user selects "Price (high to low)" from the sort dropdown
    Then the products should be sorted by price from high to low
