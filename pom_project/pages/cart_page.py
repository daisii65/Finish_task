from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://automationexercise.com/view_cart"

    def __init__(self, page):
        super().__init__(page)
        self.breadcrumb = page.get_by_text("Shopping Cart").first
        self.empty_message = page.get_by_text("Cart is empty!")
        self.cart_rows = page.locator("#cart_info_table tbody tr")
        self.product_names = page.locator(".cart_description h4 a")
        self.product_prices = page.locator(".cart_price p")
        self.product_quantity = page.locator(".cart_quantity button")
        self.product_total = page.locator(".cart_total_price")
        self.delete_button = page.locator(".cart_quantity_delete")

    def open_cart_page(self):
        self.open(self.URL)
        self.close_ad()

    def delete_first_product(self):
        self.delete_button.first.click()