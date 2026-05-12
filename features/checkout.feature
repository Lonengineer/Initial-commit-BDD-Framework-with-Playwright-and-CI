Feature: Checkout Process
  As a logged-in user
  I want to complete the checkout process
  So that I can purchase my selected products

  Background:
    Given the user is logged in and on the products page

  # Test Case 9: Verify checkout process completes successfully
  Scenario: Complete checkout process successfully
    When the user adds the first product to the cart
    And the user navigates to the cart page
    And the user clicks the checkout button
    And the user fills in checkout information with "John" "Doe" "12345"
    And the user clicks continue on checkout
    And the user clicks finish to complete the order
    Then the order completion message should be displayed
    And the completion header should say "Thank you for your order!"

  # Test Case 10: Negative test - attempt checkout with empty required fields
  Scenario: Attempt checkout with empty required fields
    When the user adds the first product to the cart
    And the user navigates to the cart page
    And the user clicks the checkout button
    And the user clicks continue on checkout without filling any fields
    Then a checkout error message should be displayed
    And the error message should contain "First Name is required"
