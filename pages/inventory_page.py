from playwright.sync_api import Page

##What we have on the page
class InventoryPage:
    def __init__(self, page:Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item-name']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")


##Action we can do on the page


def add_item_to_cart(self, item_name: str):
    self.page.locator(f"[data-test='add-to-cart-sauce-labs-{item_name}']").click()


