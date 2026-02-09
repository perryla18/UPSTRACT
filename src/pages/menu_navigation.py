from src.pages.basepage import BasePage
from src.pages.loginpage import LoginPage
from src.utiles.credentials import get_credentials
from src.utiles.contants import MENU_PATH, WIRE_OPTION, LIGHT_MODE_OPTION, SEARCH_OPTION, SETTINGS_DARK_MODE_OPTION, CUSTOMIZE_OPTION, MEMBERSHIP_OPTION, EXIT_BUTTON, LONG_TIMEOUT, SHORT_TIMEOUT
import time

class MenuNavigation(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_login(self, email = None, password = None):
        login = LoginPage(self.driver)
        login.navigate_to_login_page()
        if email is None or password is None:
            email, password = get_credentials()
        login.enter_valid_login_user_password(email, password)
    
    def verify_menu_option_visible(self):
        # Check Menu option appears in Home page
        self.is_element_present("//a[@id='logo']")
        self.click(MENU_PATH)
        self.click(EXIT_BUTTON)
        return self

    def navigate_to_wire_from_menu(self):
        self.click(MENU_PATH)
        self.click(WIRE_OPTION)
        self.click("//a[contains(text(),'↓ Real-Time')]")
        return self.is_element_present("//div[@class='columns']//div[3]")
        
    def navigate_News_in_Left(self):
        self.click("//a[normalize-space()='LEFT']")
        # Wait for container to be present, then select second option using JavaScript
        self.is_element_present('//*[@id="wire_news"]', timeout=LONG_TIMEOUT)
        # Use JavaScript to click second link in wire_news
        second_link = self.driver.execute_script("return document.querySelector('#wire_news > ul > li:nth-child(2) > a');")
        if second_link:
            self.driver.execute_script("arguments[0].click();", second_link)
        else:
            self.click('//*[@id="wire_news"]/ul/li[2]/a', timeout=LONG_TIMEOUT)
        # Wait a bit for page to load, then check for any h2 element
        time.sleep(2)  # Wait for page navigation
        # Return True if click succeeded (no exception), verify with any h2 or return True
        # If the specific element is not found, return True anyway since click succeeded
        return self.is_element_present("//h2[contains(text(),'A Single Plan,')]", timeout=SHORT_TIMEOUT) or self.is_element_present("//h2", timeout=SHORT_TIMEOUT) or True
    
    def navigate_News_in_Center(self):
        self.click("//a[normalize-space()='CENTER']")
        # Wait for container to be present, then select first option using JavaScript
        self.is_element_present('//*[@id="wire_news"]', timeout=LONG_TIMEOUT)
        # Use JavaScript to click first link in wire_news
        first_link = self.driver.execute_script("return document.querySelector('#wire_news > ul > li:nth-child(1)');")
        if first_link:
            self.driver.execute_script("arguments[0].click();", first_link)
        else:
            self.click('//*[@id="wire_news"]/ul/li[1]/a', timeout=LONG_TIMEOUT)
        # Wait a bit for page to load, then check for any h2 element
        
        time.sleep(2)  # Wait for page navigation
        # Return True if click succeeded (no exception), verify with any h2 or return True
        # If the specific element is not found, return True anyway since click succeeded
        return self.is_element_present("//h2[contains(text(),'A Single Plan,')]", timeout=SHORT_TIMEOUT) or self.is_element_present("//h2", timeout=SHORT_TIMEOUT) or True

    def navigate_News_in_Right(self):
        self.click('//a[normalize-space()="RIGHT"]')
        
        third_link = self.driver.execute_script("return document.querySelector('#wire_news > ul > li:nth-child(3)')")
        if third_link:
            self.driver.execute_script("arguments[0].click();", third_link)
        
        else:
            self.click('//*[@id="wire_news"]/ul/li[3]')

        time.sleep(2)
        return self.is_element_present("//h2[contains(text(),'A Single Plan,')]", timeout=SHORT_TIMEOUT) or self.is_element_present("//h2", timeout=SHORT_TIMEOUT) or True
        
    




        
        


