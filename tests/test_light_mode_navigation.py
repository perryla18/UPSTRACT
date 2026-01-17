import pytest
from src.pages.Light_mode import LightModeNavigation
from src.utiles.credentials import get_credentials

def test_navigate_to_Light_mode(driver):
    LightMode= LightModeNavigation(driver)
    email, password= get_credentials()
    LightMode.navigate_to_login(email, password)
    assert LightMode.go_to_menu()