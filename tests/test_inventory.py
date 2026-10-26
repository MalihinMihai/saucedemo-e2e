from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage


def test_inventory_page_products(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    
    expect(inventory_page.title).to_have_text("Products")
    expect(inventory_page.items.count()).to_be(6)