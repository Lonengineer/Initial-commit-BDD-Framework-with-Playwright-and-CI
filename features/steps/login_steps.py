# pyrefly: ignore [missing-import]
from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@given('the user is on the SauceDemo login page')
def step_open_login_page(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open_login_page()

@given('the user is logged in and on the products page')
def step_logged_in(context):
    context.login_page = LoginPage(context.page)
    context.login_page.login()
    context.products_page = ProductsPage(context.page)

@when('the user logs in with valid credentials')
def step_login_valid(context):
    context.login_page = LoginPage(context.page)
    context.login_page.login()

@then('the user should be redirected to the products page')
def step_verify_products_page(context):
    products_page = ProductsPage(context.page)
    header = products_page.get_page_header_text()
    assert header == "Products", f"Expected header 'Products', got '{header}'"

@when('the user attempts to log in with username "{username}" and password "{password}"')
def step_attempt_login_invalid(context, username, password):
    context.login_page = LoginPage(context.page)
    # Handle 'empty' string representations from feature file
    if username == "empty" or username == '""' or username == "''":
        username = ""
    if password == "empty" or password == '""' or password == "''":
        password = ""
        
    context.login_page.open_login_page()
    if username:
        context.login_page.enter_username(username)
    if password:
        context.login_page.enter_password(password)
    context.login_page.click_login()

@then('an error message containing "{expected_error}" should be displayed on the login page')
def step_verify_login_error_message(context, expected_error):
    error_message = context.login_page.get_error_message()
    assert expected_error in error_message, f"Expected error message containing '{expected_error}', but got '{error_message}'"
