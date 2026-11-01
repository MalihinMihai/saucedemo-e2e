from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from tests.conftest import ecran_login


def test_login_valid(ecran_login: LoginPage):
    ecran_login.login("standard_user", "secret_sauce")
