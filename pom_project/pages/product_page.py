from pages.base_page import BasePage

class ProductPage(BasePage):
    URL='https://automationexercise.com/products'

    def __init__(self, page):
        super().__init__(page)
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.products = page.locator(".product-image-wrapper")
        self.product_info = page.locator(".productinfo")
        self.searched_title = page.get_by_text("Searched Products")
        self.view_product_links = page.locator("a[href*='/product_details/']")
        self.product_information = page.locator(".product-information")

    def open_products(self):
        self.open(self.URL)
        self.close_ad()

    def search_product(self, product):
        self.search_input.fill(product)
        self.search_button.click()

    def open_first_product(self):
        self.view_product_links.first.click()