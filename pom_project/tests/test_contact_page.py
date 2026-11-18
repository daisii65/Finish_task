from playwright.sync_api import expect
from pages.contact_page import ContactPage


def test_open_contact_page(page):
    contact = ContactPage(page)
    contact.open_contact_page()
    assert "contact_us" in contact.get_url()


def test_contact_page_title(page):
    contact = ContactPage(page)
    contact.open_contact_page()
    assert "Automation Exercise" in contact.get_title()


def test_get_in_touch_title_visible(page):
    contact = ContactPage(page)
    contact.open_contact_page()
    expect(contact.title_text).to_be_visible()


def test_name_field_visible(page):
    contact = ContactPage(page)
    contact.open_contact_page()
    expect(contact.name_input).to_be_visible()


def test_email_field_visible(page):
    contact = ContactPage(page)
    contact.open_contact_page()
    expect(contact.email_input).to_be_visible()


def test_subject_field_visible(page):
    contact = ContactPage(page)
    contact.open_contact_page()
    expect(contact.subject_input).to_be_visible()


def test_message_field_visible(page):
    contact = ContactPage(page)
    contact.open_contact_page()
    expect(contact.message_input).to_be_visible()


def test_submit_button_visible_and_enabled(page):
    contact = ContactPage(page)
    contact.open_contact_page()
    expect(contact.submit_button).to_be_visible()
    expect(contact.submit_button).to_be_enabled()


def test_fill_form_values(page):
    contact = ContactPage(page)
    contact.open_contact_page()
    contact.fill_form("Peter", "peter@test.com", "Question", "Hello")
    expect(contact.name_input).to_have_value("Peter")
    expect(contact.email_input).to_have_value("peter@test.com")
    expect(contact.subject_input).to_have_value("Question")
    expect(contact.message_input).to_have_value("Hello")


def test_message_placeholder(page):
    contact = ContactPage(page)
    contact.open_contact_page()
    expect(contact.message_input).to_have_attribute("placeholder", "Your Message Here")