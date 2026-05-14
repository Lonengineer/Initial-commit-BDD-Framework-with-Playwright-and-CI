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

  Scenario Outline: Unsuccessful login with invalid or missing credentials
    Given the user is on the SauceDemo login page
    When the user attempts to log in with username "<username>" and password "<password>"
    Then an error message containing "<expected_error>" should be displayed on the login page

    Examples:
      | username        | password     | expected_error                                                              |
      | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out.                         |
      | invalid_user    | secret_sauce | Epic sadface: Username and password do not match any user in this service |
      | standard_user   | wrong_pass   | Epic sadface: Username and password do not match any user in this service |
      | empty           | secret_sauce | Epic sadface: Username is required                                          |
      | standard_user   | empty        | Epic sadface: Password is required                                          |
