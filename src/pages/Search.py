from src.pages.loginpage import LoginPage
from src.pages.basepage import BasePage
from src.utiles.credentials import get_credentials
from src.utiles.contants import MENU_PATH, SEARCH_OPTION, SEARCH_BOX, SEARCH_BUTTON

class SearchBox(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_login(self, email = None, password = None):
        login = LoginPage(self.driver)
        login.navigate_to_login_page()
        if email == None or password == None:
            email, password = get_credentials()
        
        login.enter_valid_login_user_password(email, password)
    
    def navigate_to_searchbox(self):
        self.click(MENU_PATH)
        self.click(SEARCH_OPTION)
        return self.is_element_present("//div[@class='mtxl mbxl']")
    
    def searching(self):
        self.send_keys(SEARCH_BOX, 'aaa')
        self.click(SEARCH_BUTTON)
        return self.is_element_present('//*[@id="content"]/div[2]/a[1]')