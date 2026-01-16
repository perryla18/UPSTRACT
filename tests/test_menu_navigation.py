import pytest
from src.pages.menu_navigation import MenuNavigation
from src.utiles.credentials import get_credentials

def test_menu_is_visible(driver):
    menu = MenuNavigation(driver)
    email,password=get_credentials()
    menu.navigate_to_login(email, password)
    
    assert menu.verify_menu_option_visible()

def test_navigate_News_Left(driver):
    menu =MenuNavigation(driver)
    email, pasword =get_credentials()
    menu.navigate_to_login(email, pasword)
# Choose WIRE Option
    menu.navigate_to_wire_from_menu()
    assert menu.navigate_News_in_Left()


