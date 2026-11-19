import pytest
from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.product_page import ProductPage


@pytest.fixture
def product_name(page):
    products = ProductPage(page)
    products.open_products()
    name = products.get_first_product_name()
    products.add_first_product_to_cart()
    return name


def test_open_cart_page(page):
    cart = CartPage(page)
    cart.open_cart_page()
    assert "view_cart" in cart.get_url()


def test_shopping_cart_breadcrumb_visible(page):
    cart = CartPage(page)
    cart.open_cart_page()
    expect(cart.breadcrumb).to_be_visible()


def test_empty_cart_message_visible(page):
    cart = CartPage(page)
    cart.open_cart_page()
    expect(cart.empty_message).to_be_visible()


def test_added_product_is_in_cart(page, product_name):
    cart = CartPage(page)
    cart.open_cart_page()
    expect(cart.cart_rows.first).to_be_visible()


def test_cart_has_one_product(page, product_name):
    cart = CartPage(page)
    cart.open_cart_page()
    expect(cart.cart_rows).to_have_count(1)


def test_product_name_in_cart_matches(page, product_name):
    cart = CartPage(page)
    cart.open_cart_page()
    expect(cart.product_names.first).to_have_text(product_name)


def test_product_price_visible(page, product_name):
    cart = CartPage(page)
    cart.open_cart_page()
    expect(cart.product_prices.first).to_be_visible()


def test_product_quantity_is_one(page, product_name):
    cart = CartPage(page)
    cart.open_cart_page()
    expect(cart.product_quantity.first).to_have_text("1")


def test_product_total_visible(page, product_name):
    cart = CartPage(page)
    cart.open_cart_page()
    expect(cart.product_total.first).to_be_visible()


def test_delete_product_makes_cart_empty(page, product_name):
    cart = CartPage(page)
    cart.open_cart_page()
    cart.delete_first_product()
    expect(cart.empty_message).to_be_visible()