from src.pages.basepage import BasePage
from src.pages.loginpage import LoginPage
from src.utiles.credentials import get_credentials
from src.utiles.contants import MENU_PATH, PROFILE_SETTING_OPTION, PROFILE_NAME, PROFILE_BIO, PROFILE_WEBSITE, NEW_PASSWORD, CURRENT_PASSWORD, CONFIRM_CHANGE_PW, ALERT_CHANGE_PW, SAVE_SETTING_BUTTON, VALID_PASSWORD

class ProfileSetting(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_login(self, email = None, password = None):
        login = LoginPage(self.driver)
        login.navigate_to_login_page()
        if email is None or password is None:
            email,password = get_credentials()
        login.enter_valid_login_user_password(email, password)

    def navigate_to_profile_setting(self):
        self.click(MENU_PATH)
        self.click(PROFILE_SETTING_OPTION)
        return self.is_element_present("//h2[normalize-space()='Your Account Profile']")
    
    def change_setting(self):
        self.send_keys(PROFILE_NAME, "AndorineLa")
        self.send_keys(PROFILE_BIO, "Andorine with your happinest")
        self.send_keys(PROFILE_WEBSITE, "http://myandorine.com")
        self.click(SAVE_SETTING_BUTTON)
        return self.is_element_present("//a[@id='logo']")

    def change_pw(self):
        self.send_keys(CURRENT_PASSWORD, VALID_PASSWORD)
        self.send_keys(NEW_PASSWORD, VALID_PASSWORD)
        self.click(CONFIRM_CHANGE_PW)
        return self.is_element_present(ALERT_CHANGE_PW)
    

