from dotenv import load_dotenv
load_dotenv()

import os

import pytest
from playwright.sync_api import Browser, Page

from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def auth_state(browser: Browser, base_url: str) -> str:
    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    page.goto("/")
    page.get_by_placeholder("Username").fill(os.environ["SAUCE_USER"])
    page.get_by_placeholder("Password").fill(os.environ["SAUCE_PASSWORD"])
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/inventory.html")

@pytest.fixture
def ecran_login(page: Page) -> LoginPage:
    lp = LoginPage(page)
    lp.open()
    return lp

