import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Browser, Page

from pages.login_page import LoginPage

load_dotenv()

AUTH_FILE = "auth/standard_user.json"


@pytest.fixture(scope="session")
def auth_state(browser: Browser, base_url: str, browser_name: str, worker_id: str) -> str:
    os.makedirs("auth", exist_ok=True)
    path = f"auth/{browser_name}_{worker_id}.json"
    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    page.goto("/")
    page.get_by_placeholder("Username").fill(os.environ["SAUCE_USER"])
    page.get_by_placeholder("Password").fill(os.environ["SAUCE_PASSWORD"])
    page.get_by_role("button", name="Login").click()
    page.wait_for_url("**/inventory.html")
    context.storage_state(path=path)
    context.close()
    return path


@pytest.fixture
def logged_in_page(new_context, auth_state: str) -> Page:
    context = new_context(storage_state=auth_state)
    page = context.new_page()
    page.goto("/inventory.html")
    return page


@pytest.fixture
def ecran_login(page: Page) -> LoginPage:
    lp = LoginPage(page)
    lp.open()
    return lp