import pytest
from src.utiles.credentials import get_credentials
from src.pages.Search import SearchBox

def test_navigate_to_searchbox(driver):
    searchbox = SearchBox(driver)
    email, password = get_credentials()
    searchbox.navigate_to_login(email, password)
    assert searchbox.navigate_to_searchbox()

def test_search_result(driver):
    searchbox = SearchBox(driver)
    email, password = get_credentials()
    searchbox.navigate_to_login(email, password)
    searchbox.navigate_to_searchbox()
    assert searchbox.searching()