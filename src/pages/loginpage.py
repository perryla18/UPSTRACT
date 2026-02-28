from src.pages.basepage import BasePage
from src.utiles.credentials import get_credentials, get_invalid_credentials, get_username, get_password
from src.utiles.contants import BASE_URL, MENU_PATH, LOGIN_AND_SIGNUP_OPTION, LOGIN_LOGO, INPUT_EMAIL_LOGIN, INPUT_PW_LOGIN, LOGIN_BUTTON, SHORT_TIMEOUT


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_login_page(self):
        self.navigate_to_url(BASE_URL)
        self.click(MENU_PATH)
        self.click(LOGIN_AND_SIGNUP_OPTION)
        return self.is_element_present(LOGIN_LOGO)

    def enter_valid_login_user_password(self, email = None, password = None):
        if email is None or password is None:
            email, password = get_credentials()
        
        self.send_keys(INPUT_EMAIL_LOGIN, email)
        self.send_keys(INPUT_PW_LOGIN, password)
        self.click(LOGIN_BUTTON)
        return self.is_element_present("//a[@id='logo']")
    
    def enter_invalid_credentials(self, email = None, password=None):
        if email is None or password is None:
            email, password = get_invalid_credentials()

        self.send_keys(INPUT_EMAIL_LOGIN, email)
        self.send_keys(INPUT_PW_LOGIN, password)
        self.click(LOGIN_BUTTON)
        return self.is_element_present("//div[@class='toast-error']")

    def enter_email_or_password_only_blank(self, email = None, password = None):
        """
        Test case: Nhập chỉ email hoặc chỉ password để test validation
        - Case 1: Chỉ nhập password (email là None hoặc empty)
        - Case 2: Chỉ nhập email (password là None hoặc empty)
        - Case 3: Cả hai đều empty
        """
        if email is None or email == "":
            if email == "":
                self.send_keys(INPUT_EMAIL_LOGIN, email)
            if password is None:
                password = get_password()
            self.send_keys(INPUT_PW_LOGIN, password)
            self.click(LOGIN_BUTTON)
        elif password is None or password == "":
            if email is None:
                email = get_username()
            self.send_keys(INPUT_EMAIL_LOGIN, email)
            if password == '':
                self.send_keys(INPUT_PW_LOGIN, password)
            self.click(LOGIN_BUTTON)
        else:
            self.send_keys(INPUT_EMAIL_LOGIN, email)
            self.send_keys(INPUT_PW_LOGIN, password)
            self.click(LOGIN_BUTTON)
        
        # Sử dụng helper method để kiểm tra validation error
        return self.check_validation_error(INPUT_EMAIL_LOGIN, INPUT_PW_LOGIN, SHORT_TIMEOUT)
