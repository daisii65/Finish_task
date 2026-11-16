from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "/"

    def __init__(self, page):
        super().__init__(page)
        self.products_link = page.locator("a[href='/products']")
        self.login_link = page.locator("a[href='/login']")
        self.contact_us_link = page.locator("a[href='/contact_us']")
        self.featured_products = page.locator(".features_items")

    def open_home_page(self): 
        self.open(self.URL)

    def go_to_products(self): 
        self.products_link.click()

    def go_to_login(self): 
        self.login_link.click()

    def go_to_contact_us(self): 
        self.contact_us_link.click()       

