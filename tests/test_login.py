import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from tests.conftest import ecran_login


#@pytest.mark.smoke
#def test_login_valid(ecran_login: LoginPage):
    #ecran_login.login("standard_user", "secret_sauce")


@pytest.mark.parametrize("user,password,error",
    [("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
     (" ", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
     ("", "", "Epic sadface: Username is required"),
     ("standard_user", "", "Epic sadface: Password is required")])
def test_login_errors(ecran_login, user, password, error):
    ecran_login.login(user, password)
    expect(ecran_login.error_message).to_have_text(error)

