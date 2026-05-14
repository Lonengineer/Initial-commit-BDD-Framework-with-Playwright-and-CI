# pyrefly: ignore [missing-import]
from behave import when, then
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@when('the user clicks the checkout button')
def step_click_checkout(context):
    context.cart_page = CartPage(context.page)
    context.cart_page.click_checkout()

@when('the user fills in checkout information with "{first_name}" "{last_name}" "{postal_code}"')
def step_fill_checkout_info(context, first_name, last_name, postal_code):
    context.checkout_page = CheckoutPage(context.page)
    
    if first_name == "empty" or first_name == '""' or first_name == "''":
        first_name = ""
    if last_name == "empty" or last_name == '""' or last_name == "''":
        last_name = ""
    if postal_code == "empty" or postal_code == '""' or postal_code == "''":
        postal_code = ""
        
    context.checkout_page.fill_checkout_information(first_name, last_name, postal_code)

@when('the user clicks continue on checkout')
def step_click_continue(context):
    context.checkout_page = CheckoutPage(context.page)
    context.checkout_page.click_continue()



@when('the user clicks finish to complete the order')
def step_click_finish(context):
    context.checkout_page = CheckoutPage(context.page)
    context.checkout_page.click_finish()

@then('the order completion message should be displayed')
def step_verify_order_completion(context):
    checkout_page = CheckoutPage(context.page)
    assert checkout_page.is_checkout_complete() is True, "Checkout completion message not displayed."

@then('the completion header should say "{expected_header}"')
def step_verify_completion_header(context, expected_header):
    checkout_page = CheckoutPage(context.page)
    actual_header = checkout_page.get_complete_header()
    assert actual_header == expected_header, f"Expected '{expected_header}', got '{actual_header}'"

@then('a checkout error message should be displayed')
def step_verify_checkout_error(context):
    checkout_page = CheckoutPage(context.page)
    error_msg = checkout_page.get_checkout_error_message()
    assert error_msg is not None and len(error_msg) > 0, "Expected an error message but none was displayed."

@then('the error message should contain "{error_text}"')
def step_verify_error_text(context, error_text):
    checkout_page = CheckoutPage(context.page)
    actual_error = checkout_page.get_checkout_error_message()
    assert error_text in actual_error, f"Expected error to contain '{error_text}', got '{actual_error}'"

@then('the total price should be "{expected_total}"')
def step_verify_total_price(context, expected_total):
    checkout_page = CheckoutPage(context.page)
    actual_total = checkout_page.get_total_price()
    assert expected_total in actual_total, f"Expected total to contain '{expected_total}', got '{actual_total}'"
