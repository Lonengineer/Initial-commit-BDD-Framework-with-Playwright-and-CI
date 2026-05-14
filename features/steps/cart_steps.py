
# pyrefly: ignore [missing-import]
from behave import when, then
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@when('the user adds the first product to the cart')
def step_add_first_product(context):
    context.products_page = ProductsPage(context.page)
    context.products_page.add_product_to_cart_by_index(0)


@when('the user adds another product to the cart')
def step_add_another_product(context):
    context.products_page = ProductsPage(context.page)
    context.products_page.add_product_to_cart_by_index(1)

@when('the user adds {count:d} products to the cart')
def step_add_multiple_products(context, count):
    context.products_page = ProductsPage(context.page)
    context.products_page.add_multiple_products_to_cart(count)

@when('the user navigates to the cart page')
def step_navigate_to_cart(context):
    context.products_page = ProductsPage(context.page)
    context.products_page.go_to_cart()
    context.cart_page = CartPage(context.page)

@when('the user removes the first item from the cart')
def step_remove_first_item(context):
    context.cart_page = CartPage(context.page)
    context.cart_page.remove_item_by_index(0)

@when('the user removes all items from the cart')
def step_remove_all_items(context):
    context.cart_page = CartPage(context.page)
    context.cart_page.remove_all_items()

@then('the cart badge should display "{count}"')
def step_verify_cart_badge(context, count):
    products_page = ProductsPage(context.page)
    actual_count = products_page.get_cart_badge_count()
    assert str(actual_count) == count, f"Expected cart badge to show '{count}', but got '{actual_count}'."

@then('the cart should contain {count:d} items')
def step_verify_cart_item_count(context, count):
    if "cart.html" not in context.page.url:
        products_page = ProductsPage(context.page)
        products_page.go_to_cart()
        
    cart_page = CartPage(context.page)
    actual_count = cart_page.get_cart_item_count()
    assert actual_count == count, f"Expected {count} items in cart, but found {actual_count}."

@then('the cart should be empty')
def step_verify_cart_empty(context):
    cart_page = CartPage(context.page)
    is_empty = cart_page.is_cart_empty()
    assert is_empty is True, "Expected cart to be empty, but it has items."

@then('the cart badge should not be displayed')
def step_verify_cart_badge_hidden(context):
    products_page = ProductsPage(context.page)
    is_displayed = products_page.is_cart_badge_displayed()
    assert is_displayed is False, "Expected cart badge to be hidden, but it was displayed."

@then('the add to cart button for the first product should become "{expected_text}"')
def step_verify_button_text(context, expected_text):
    products_page = ProductsPage(context.page)
    actual_text = products_page.get_product_button_text_by_index(0)
    assert actual_text == expected_text, f"Expected button text '{expected_text}', got '{actual_text}'"

