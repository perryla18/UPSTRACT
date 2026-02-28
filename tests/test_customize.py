import pytest
from src.pages.customize import CustomizePage
from src.utiles.credentials import get_credentials

def test_navigate_to_customize_page(driver):
    custome = CustomizePage(driver)
    email, password = get_credentials()
    custome.navigate_to_login(email, password)
    assert custome.navigate_to_customize()

def test_remove_customize(driver):
    custome = CustomizePage(driver)
    email, password = get_credentials()
    custome.navigate_to_login(email, password)
    custome.navigate_to_customize()
    assert custome.remove_customize()