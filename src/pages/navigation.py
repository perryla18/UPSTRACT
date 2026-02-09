from src.pages.basepage import BasePage
from src.pages.loginpage import LoginPage
from src.utiles.credentials import get_credentials

class Navigation(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_login(self, email = None, password = None):
        login = LoginPage(self.driver)
        login.navigate_to_login_page()
        if email is None or password is None:
            email, password = get_credentials()
        login.enter_valid_login_user_password(email, password)
    

    def navigate_to_reddit(self):
        initial_handles = list(self.driver.window_handles)
        self.click("//h4[normalize-space()='Reddit']")
        self.switch_to_new_window_if_opened(initial_handles)
        self.wait_for_url_contains("reddit.com")
        return self.get_link("https://www.reddit.com/")

    def navigate_to_yahoo(self):
        initial_handles = list(self.driver.window_handles)
        self.click("//h4[normalize-space()='Yahoo News']")
        self.switch_to_new_window_if_opened(initial_handles)
        assert self.wait_for_url_contains("news.yahoo.com")