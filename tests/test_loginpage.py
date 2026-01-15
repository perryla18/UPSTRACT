import pytest
from src.pages.loginpage import LoginPage
from src.utiles.credentials import get_credentials, get_invalid_credentials, get_username, get_password

def test_valid_credential(driver):
    login = LoginPage(driver)
    login.navigate_to_login_page()
    email, password = get_credentials()
    assert login.enter_valid_login_user_password(email, password)

def test_invalid_credential(driver):
    login = LoginPage(driver)
    login.navigate_to_login_page()
    email, password = get_invalid_credentials()
    assert login.enter_invalid_credentials(email, password)

def test_with_user_empty(driver):
    login=LoginPage(driver)
    login.navigate_to_login_page()
    email = ''
    pasword = get_password()
    assert login.enter_email_or_password_only_blank(email, pasword)