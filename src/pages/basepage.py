from selenium.webdriver.common.by import By
from src.utiles.helpers import (
    wait_for_element,
    wait_for_element_clickable,
    click_element,
    sends_key_to_element,
    get_element_text,
    is_element_present,
    get_current_url,
    get_page_title,
    take_screenshot)

from src.utiles.contants import DEFAULT_TIMEOUT, SHORT_TIMEOUT

class BasePage():
    def __init__(self, driver):
        self.driver = driver

# ============================================
# ELEMENT METHODS (wrap từ helpers.py)
# ============================================   

    def find_element(self, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
        return wait_for_element(self.driver, locator, timeout, by)

    def click(self, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
        return click_element(self.driver, locator, timeout, by)

    def send_keys(self, locator, text, timeout = DEFAULT_TIMEOUT, by = By.XPATH, clear_first=True):
        return sends_key_to_element(self.driver, locator, text, timeout, by, clear_first)

    def get_text(self, locator, timeout=DEFAULT_TIMEOUT, by=By.XPATH):
        return get_element_text(self.driver, locator, timeout, by)

    def is_element_present(self, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
        return is_element_present(self.driver, locator, timeout, by)

    def is_waiting_for_element(self, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
        return wait_for_element(self.driver, locator, timeout, by)

    # ============================================
    # BROWSER METHODS
    # ============================================

    def navigate_to_url(self, url):
        """Navigate to a specific URL"""
        self.driver.get(url)

    def get_url(self):
        return get_current_url(self.driver)

    def get_title(self):
        return get_page_title(self.driver)

    
    # ============================================
    # SCREENSHOT 
    # ============================================

    def take_screenshot(self, filename=None):
        return take_screenshot(self.driver, filename)
    
    # ============================================
    # Check login validation
    # ============================================
    def check_validation_error(driver, email_input_locator, password_input_locator, timeout=SHORT_TIMEOUT):
        """
    Kiểm tra validation error bằng nhiều cách:
    1. Thử nhiều locator phổ biến cho error messages
    2. Kiểm tra HTML5 validation state
    3. Kiểm tra invalid state của input fields
    
    Args:
        driver: WebDriver instance
        email_input_locator: Locator cho email input field
        password_input_locator: Locator cho password input field
        timeout: Timeout cho việc tìm elements
    
    Returns:
        bool: True nếu tìm thấy validation error, False nếu không
        """
    # Danh sách các locator phổ biến cho validation errors
        error_locators = [
            "//div[@class='toast-error']",
            "//div[contains(@class, 'error')]",
            "//div[contains(@class, 'invalid')]",
            "//span[contains(@class, 'error')]",
            "//span[contains(@class, 'invalid')]",
            "//div[contains(@class, 'validation')]",
            "//div[contains(@class, 'required')]",
            "//*[contains(text(), 'required')]",
            "//*[contains(text(), 'Required')]",
            "//*[contains(text(), 'invalid')]",
            "//*[contains(text(), 'Invalid')]",
        ]
        
        # Thử từng locator
        for locator in error_locators:
            if is_element_present(driver, locator, timeout=timeout):
                return True
        
        # Kiểm tra HTML5 validation state
        try:
            email_input = wait_for_element(driver, email_input_locator, timeout=timeout)
            password_input = wait_for_element(driver, password_input_locator, timeout=timeout)
            
            # Kiểm tra xem input có invalid state không
            email_invalid = driver.execute_script("return arguments[0].validity.valid === false;", email_input)
            password_invalid = driver.execute_script("return arguments[0].validity.valid === false;", password_input)
            
            if email_invalid or password_invalid:
                return True
        except:
            pass
        
        return False


