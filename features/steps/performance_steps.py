import time
from behave import given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@given('the user measures the page load start time')
def step_measure_start_time(context):
    context.start_time = time.time()

@when('the user opens the SauceDemo login page')
def step_open_login_page_perf(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open_login_page()

@then('the login page should load within {seconds:d} seconds')
def step_verify_login_load_time(context, seconds):
    context.login_page = LoginPage(context.page)
    # Wait for username input to be visible to confirm page load
    is_visible = context.login_page.is_element_displayed(context.login_page.USERNAME_INPUT)
    assert is_visible, "Login page did not load properly."
    
    end_time = time.time()
    load_time = end_time - context.start_time
    context.logger.info(f"Login page load time: {load_time:.2f} seconds")
    assert load_time <= seconds, f"Login page took {load_time:.2f}s to load, expected <= {seconds}s"

@then('the products page should load within {seconds:d} seconds')
def step_verify_products_load_time(context, seconds):
    products_page = ProductsPage(context.page)
    # Wait for product title to confirm page load
    header = products_page.get_page_header_text()
    assert header == "Products", "Products page did not load properly."
    
    end_time = time.time()
    load_time = end_time - context.start_time
    context.logger.info(f"Products page load time: {load_time:.2f} seconds")
    assert load_time <= seconds, f"Products page took {load_time:.2f}s to load, expected <= {seconds}s"
