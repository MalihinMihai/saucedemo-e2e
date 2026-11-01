from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator("[data-test='inventory-item-name']")
        self.checkout_button = page.locator("[data-test='checkout']")

    def open(self):
        self.page.goto("/cart.html")

    def checkout(self):
        self.checkout_button.click()

    