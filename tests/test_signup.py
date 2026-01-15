import pytest
from src.pages.signup import SignUp
from src.utiles.credentials import get_credentials

def test_navigate_to_sign_up(driver):
    SignUpNavigate = SignUp(driver)
    SignUpNavigate.navigate_to_UPSTRACT_page()
    assert SignUpNavigate.navigate_to_signup_page()
    
    email, password = get_credentials()
    SignUpNavigate.enter_email_pw(email, password)
    assert SignUpNavigate.set_user_name()
