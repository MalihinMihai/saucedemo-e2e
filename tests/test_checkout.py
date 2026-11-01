from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


def test_checkout_process(logged_in_page: Page):
    iventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    iventory_page.add_item_to_cart("backpack")
    iventory_page.add_item_to_cart("bike-light")

    cart_page.open()
    expect(cart_page.items).to_have_count(2)

    cart_page.checkout()
    checkout_page.fill_information("John", "Doe", "12345")
    checkout_page.finish_order()