from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page:Page):
        self.page = page
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test]='inventory-item-name'")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")


    #Define methods.

    def _item(self, product_name : str):
        return self.items.filter(has_text=product_name)


        


