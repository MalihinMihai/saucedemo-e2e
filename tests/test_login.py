from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_valid(ecran_login: LoginPage, page: Page):
    ecran_login.login("standard_user", "secret_sauce")
