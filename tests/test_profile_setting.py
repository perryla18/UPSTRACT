import pytest
from src.pages.profilesetting import ProfileSetting
from src.utiles.credentials import get_credentials

def test_navigate_to_profilesetting(driver):
    profile = ProfileSetting(driver)
    email, pasword = get_credentials()
    profile.navigate_to_login(email,pasword)
    assert profile.navigate_to_profile_setting()

def test_change_setting(driver):
    profile = ProfileSetting(driver)
    email, pasword = get_credentials()
    profile.navigate_to_login(email,pasword)
    profile.navigate_to_profile_setting()
    assert profile.change_setting()

def test_change_pw(driver):
    profile = ProfileSetting(driver)
    email, pasword = get_credentials()
    profile.navigate_to_login(email,pasword)
    profile.navigate_to_profile_setting()
    assert profile.change_pw()