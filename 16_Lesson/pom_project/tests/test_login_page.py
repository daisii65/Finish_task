from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_open_login_page(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    assert "login" in login_page.get_url()

def test_email_field_visible(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    expect(login_page.email_input).to_be_visible()

def test_password_field_visible(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    expect(login_page.password_input).to_be_visible()

def test_login_button_visible(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    expect(login_page.login_button).to_be_visible()

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login("123@df.er", "123")
    expect(login_page.error_message).to_be_visible()

