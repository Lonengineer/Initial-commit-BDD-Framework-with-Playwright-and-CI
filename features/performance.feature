Feature: Performance Testing
  As a user of SauceDemo
  I want the pages to load quickly
  So that I have a smooth user experience

  # Test Case 12: Verify homepage/product page loads within acceptable time
  Scenario: Login page loads within acceptable time
    Given the user measures the page load start time
    When the user opens the SauceDemo login page
    Then the login page should load within 5 seconds

  Scenario: Products page loads within acceptable time after login
    Given the user is on the SauceDemo login page
    And the user measures the page load start time
    When the user logs in with valid credentials
    Then the products page should load within 5 seconds
