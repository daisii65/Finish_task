from playwright.sync_api import expect
from pages.product_page import ProductPage


def test_open_products_page(page):
    products = ProductPage(page)
    products.open_products()
    assert "/products" in products.get_url()


def test_products_page_title(page):
    products = ProductPage(page)
    products.open_products()
    assert "Automation Exercise" in products.get_title()


def test_search_input_visible(page):
    products = ProductPage(page)
    products.open_products()
    expect(products.search_input).to_be_visible()


def test_search_button_visible(page):
    products = ProductPage(page)
    products.open_products()
    expect(products.search_button).to_be_visible()


def test_products_list_not_empty(page):
    products = ProductPage(page)
    products.open_products()
    assert products.products.count() > 0


def test_search_shows_searched_products_title(page):
    products = ProductPage(page)
    products.open_products()
    products.search_product("Blue Top")
    expect(products.searched_title).to_be_visible()


def test_search_result_contains_product(page):
    products = ProductPage(page)
    products.open_products()
    products.search_product("Blue Top")
    expect(products.product_info.first).to_contain_text("Blue Top", ignore_case=True)


def test_search_nonexistent_product(page):
    products = ProductPage(page)
    products.open_products()
    products.search_product("zzzzzzzz")
    expect(products.products).to_have_count(0)


def test_search_input_keeps_value(page):
    products = ProductPage(page)
    products.open_products()
    products.search_input.fill("Blue Top")
    expect(products.search_input).to_have_value("Blue Top")


def test_open_first_product(page):
    products = ProductPage(page)
    products.open_products()
    products.open_first_product()
    assert "/product_details/" in products.get_url()
    expect(products.product_information).to_be_visible()