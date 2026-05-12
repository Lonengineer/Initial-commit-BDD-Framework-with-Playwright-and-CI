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
