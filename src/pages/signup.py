from src.utiles.credentials import get_credentials
from src.utiles.contants import BASE_URL, MENU_PATH, LOGIN_AND_SIGNUP_OPTION, SIGNUP_LOGO, INPUT_EMAIL, INPUT_PW, SIGNUP_BUTTON
from src.pages.basepage import BasePage

class SignUp(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_UPSTRACT_page(self):
        self.navigate_to_url(BASE_URL)
    
    def navigate_to_signup_page(self):
        self.click(MENU_PATH)
        self.click(LOGIN_AND_SIGNUP_OPTION)
        return self.is_element_present(SIGNUP_LOGO)
    
    def enter_email_pw(self, email=None, password=None):
        if email is None or password is None:
            email, password = get_credentials()
        
        self.send_keys(INPUT_EMAIL, email)
        self.send_keys(INPUT_PW, password)
        self.click(SIGNUP_BUTTON)
        return self.is_element_present("//div[@class='mtxl mbxl']")
    
    def set_user_name(self):
        self.send_keys("//input[@placeholder='A-Z & 0-9 (2 Minimum)']", 'Andorine')
        self.click("//button[normalize-space()='Save']")
        return self.is_element_present("//h2[contains(text(),'A Single Plan,')]")
