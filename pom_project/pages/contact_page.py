from pages.base_page import BasePage


class ContactPage(BasePage):
    URL = "https://automationexercise.com/contact_us"

    def __init__(self, page):
        super().__init__(page)
        self.title_text = page.get_by_text("Get In Touch")
        self.name_input = page.locator("[data-qa='name']")
        self.email_input = page.locator("[data-qa='email']")
        self.subject_input = page.locator("[data-qa='subject']")
        self.message_input = page.locator("[data-qa='message']")
        self.submit_button = page.locator("[data-qa='submit-button']")

    def open_contact_page(self):
        self.open(self.URL)
        self.close_ad()

    def enter_name(self, name):
        self.name_input.fill(name)

    def enter_email(self, email):
        self.email_input.fill(email)

    def enter_subject(self, subject):
        self.subject_input.fill(subject)

    def enter_message(self, message):
        self.message_input.fill(message)

    def fill_form(self, name, email, subject, message):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_subject(subject)
        self.enter_message(message)

    # def test_file_upload(page):
    # page.goto("https://automationexercise.com/contact_us")

    # page.locator("#file-upload").set_input_files(r"D:\SmartApp\BGaming\upload_download\17.pdf")

    # page.locator("#file-submit").click()

    # expect(page.locator("#uploaded-files")).to_have_text("17.pdf")
    
   