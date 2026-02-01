from src.pages.navigation import Navigation
from src.utiles.credentials import get_credentials
import pytest

def test_navigate_to_reddit(driver):
    reddit = Navigation(driver)
    email, password = get_credentials()
    reddit.navigate_to_login(email, password)
    assert reddit.navigate_to_reddit()
    