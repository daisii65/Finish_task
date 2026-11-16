from playwright.sync_api import expect
from pages.home_page import HomePage

def test_open_home_page(page):
    h = HomePage(page) 
    h.open_home_page() 
    assert 'Automation Exercise' in h.get_title()

def test_featured_products_visible(page):
    h = HomePage(page)
    h.open_home_page() 
    expect(h.featured_products).to_be_visible()

def test_navigation_to_products(page):
    h = HomePage(page)
    h.open_home_page()
    h.go_to_products()
    assert '/products' not in h.get_url()
    expect(page).to_have_url('https://automationexercise.com/products')

def test_navigation_to_login(page):
    h = HomePage(page)
    h.open_home_page()
    h.go_to_login()
    assert '/login' in h.get_url()
    expect(page).to_have_url('https://automationexercise.com/login')

def test_navigation_to_contact(page):
    h = HomePage(page)
    h.open_home_page()
    h.go_to_contact_us()
    assert '/contact_us' in h.get_url()
    expect(page).to_have_url('https://automationexercise.com/contact_us')
