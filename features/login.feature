Feature: User Login
  As a user of SauceDemo
  I want to log in to the application
  So that I can access the products page

  # Note: Login is used as a prerequisite step for other tests.
  # This feature validates that login works correctly before other tests depend on it.

  Scenario: Successful login with valid credentials
    Given the user is on the SauceDemo login page
    When the user logs in with valid credentials
    Then the user should be redirected to the products page
