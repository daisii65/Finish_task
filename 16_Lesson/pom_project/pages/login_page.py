from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://automationexercise.com/login"

    def __init__(self,page):
        super().__init__(page)
        self.email_input=page.locator("input[data-qa='login-email']")
        self.password_input=page.locator("input[data-qa='login-password']")
        self.login_button=page.locator("button[data-qa='login-button']")
        self.error_message=page.locator('.login-form p')

    def open_login_page(self): 
        self.open(self.URL)
    
    def enter_email(self, email): 
        self.email_input.fill(email)
    
    def enter_password(self, password): 
        self.password_input.fill(password)
    
    def click_login(self): 
        self.login_button.click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
