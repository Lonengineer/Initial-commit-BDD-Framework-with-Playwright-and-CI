from behave import when, then
from pages.products_page import ProductsPage

@when('the user selects "{option}" from the sort dropdown')
def step_select_sort_option(context, option):
    context.products_page = ProductsPage(context.page)
    context.products_page.select_sort_option(option)

@then('the products should be sorted alphabetically from A to Z')
def step_verify_sort_az(context):
    products_page = ProductsPage(context.page)
    names = products_page.get_product_names()
    assert len(names) > 0, "No products found on page."
    
    # Check if the list is sorted in ascending order
    sorted_names = sorted(names)
    assert names == sorted_names, f"Products not sorted A-Z. \nActual: {names}\nExpected: {sorted_names}"

@then('the products should be sorted alphabetically from Z to A')
def step_verify_sort_za(context):
    products_page = ProductsPage(context.page)
    names = products_page.get_product_names()
    assert len(names) > 0, "No products found on page."
    
    # Check if the list is sorted in descending order
    sorted_names = sorted(names, reverse=True)
    assert names == sorted_names, f"Products not sorted Z-A. \nActual: {names}\nExpected: {sorted_names}"

@then('the products should be sorted by price from low to high')
def step_verify_sort_low_high(context):
    products_page = ProductsPage(context.page)
    prices = products_page.get_product_prices()
    assert len(prices) > 0, "No products found on page."
    
    # Check if prices are sorted low to high
    sorted_prices = sorted(prices)
    assert prices == sorted_prices, f"Products not sorted low-high. \nActual: {prices}\nExpected: {sorted_prices}"

@then('the products should be sorted by price from high to low')
def step_verify_sort_high_low(context):
    products_page = ProductsPage(context.page)
    prices = products_page.get_product_prices()
    assert len(prices) > 0, "No products found on page."
    
    # Check if prices are sorted high to low
    sorted_prices = sorted(prices, reverse=True)
    assert prices == sorted_prices, f"Products not sorted high-low. \nActual: {prices}\nExpected: {sorted_prices}"
