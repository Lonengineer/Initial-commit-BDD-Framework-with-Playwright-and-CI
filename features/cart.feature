Feature: Shopping Cart
  As a logged-in user
  I want to manage products in my shopping cart
  So that I can purchase the items I want

  Background:
    Given the user is logged in and on the products page

  # Test Case 5: Verify a product can be added to cart
  Scenario: Add a single product to the cart
    When the user adds the first product to the cart
    Then the cart badge should display "1"

  # Test Case 6: Verify multiple products can be added to cart
  Scenario: Add multiple products to the cart
    When the user adds 3 products to the cart
    Then the cart badge should display "3"
    And the cart should contain 3 items

  # Test Case 7: Verify a product can be removed from cart
  Scenario: Remove a product from the cart
    When the user adds the first product to the cart
    And the user navigates to the cart page
    And the user removes the first item from the cart
    Then the cart should be empty

  # Test Case 8: Verify cart badge updates correctly after adding items
  Scenario: Cart badge updates correctly when adding items
    When the user adds the first product to the cart
    Then the cart badge should display "1"
    When the user adds another product to the cart
    Then the cart badge should display "2"

  # Test Case 11: Negative test - remove all products and verify cart becomes empty
  Scenario: Remove all products and verify cart becomes empty
    When the user adds 3 products to the cart
    And the user navigates to the cart page
    And the user removes all items from the cart
    Then the cart should be empty
    And the cart badge should not be displayed
