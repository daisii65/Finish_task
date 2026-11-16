from pages.base_page import BasePage

class ProductPage(BasePage):
    URL='https://automationexercise.com/products'

    def __init__(self,page):
        super().__init__(page)
        self.search_input=page.locator('#search_product')
        self.search_button=page.locator('#submit_search')
        self.products=page.locator('.product-image-wrapper')
        self.searched_products_title=page.locator('.title.text-center')
        self.product_information=page.locator('.product-information')
        self.product_names=page.locator('.product-information h2')

    def open_products(self): 
        pass

    def search_product(self,product):
        pass

    def open_first_product(self): 
        pass
