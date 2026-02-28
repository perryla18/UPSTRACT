from src.pages.basepage import BasePage
from src.pages.loginpage import LoginPage
from src.utiles.credentials import get_credentials
from src.utiles.contants import MENU_PATH, CUSTOMIZE_OPTION, REMOVE_BUTTON, ALERT_CUSTOMIZE

class CustomizePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_login(self, email = None, password = None):
        login = LoginPage(self.driver)
        login.navigate_to_login_page()
        if email is None or password is None:
            email, password = get_credentials()
        login.enter_valid_login_user_password(email, password)
    
    def navigate_to_customize(self):
        self.click(MENU_PATH)
        self.click(CUSTOMIZE_OPTION)
        return self.is_element_present(ALERT_CUSTOMIZE)
    
    def remove_customize(self):
        self.click(REMOVE_BUTTON)
        return self.is_element_present("//h2[contains(text(),'A Single Plan,')]")
