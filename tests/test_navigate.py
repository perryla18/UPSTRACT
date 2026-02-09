from src.pages.navigation import Navigation
from src.utiles.credentials import get_credentials
import pytest

def test_navigate_to_reddit(driver):
    reddit = Navigation(driver)
    email, password = get_credentials()
    reddit.navigate_to_login(email, password)
    assert reddit.navigate_to_reddit()

def test_navigate_to_yahoo(driver):
    yahoo = Navigation(driver)
    email, password = get_credentials()
    yahoo.navigate_to_login(email, password)
    assert yahoo.navigate_to_yahoo()
    