from src.pages.basepage import BasePage
from src.pages.loginpage import LoginPage
from src.utiles.credentials import get_credentials
from src.utiles.contants import LIGHT_MODE_OPTION,MENU_PATH


class LightModeNavigation(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_login(self,email,password):
        login = LoginPage(self.driver)
        login.navigate_to_login_page()
        if email is None or password is None:
            email, password = get_credentials()
        login.enter_valid_login_user_password(email, password)

    def go_to_menu(self):
        self.click(MENU_PATH)
        self.click(LIGHT_MODE_OPTION)
        return self.is_element_present("//body//ul//li[1]")
        