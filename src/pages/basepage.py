import time
from selenium.webdriver.common.by import By
from src.utiles.helpers import (
    wait_for_element,
    wait_for_element_clickable,
    click_element,
    sends_key_to_element,
    get_element_text,
    is_element_present,
    get_current_url,
    get_link,
    get_page_title,
    take_screenshot)

from src.utiles.contants import DEFAULT_TIMEOUT, SHORT_TIMEOUT, LONG_TIMEOUT

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

    def is_waiting_for_element(self, locator, timeout=LONG_TIMEOUT, by = By.XPATH):
        return wait_for_element(self.driver, locator, timeout, by)

    # ============================================
    # BROWSER METHODS
    # ============================================

    def navigate_to_url(self, url):
        """Navigate to a specific URL"""
        self.driver.get(url)

    def get_url(self):
        return get_current_url(self.driver)
    
    def get_link(self, url):
        return get_link(self.driver, url)

    def get_title(self):
        return get_page_title(self.driver)
    
    def switch_to_new_window_if_opened(self, initial_handles = None, timeout = DEFAULT_TIMEOUT):
        # 👉 initial_handles = danh sách tab/window trước khi click
        if initial_handles is None:
            # Nếu không truyền vào → set thành list rỗng để tránh lỗi.
            initial_handles = []
            # → Cho hàm chạy tối đa timeout giây
        end_time = time.time() + timeout
        # → Loop liên tục cho đến khi:
        # Tìm thấy tab mới
        # Hoặc hết thời gian
        while time.time() < end_time:
            # lấy danh sách window hiện tại
            handles = self.driver.window_handles
                # 👉 Nếu handle không tồn tại trong danh sách ban đầu → Đây chính là tab mới
            for h in handles:
                if h not in initial_handles:
                    self.driver.switch_to.window(h)
                    return True
                time.sleep(0.3)
            return False
    
    def wait_for_url_contains(self, substring, timeout=DEFAULT_TIMEOUT):
        """Wait until current URL contains substring. Returns True if found."""
        end_time = time.time() + timeout
        while time.time() < end_time:
            if substring in self.driver.current_url:
                return True
            time.sleep(0.3)
        return False

    
    # ============================================
    # SCREENSHOT 
    # ============================================

    def take_screenshot(self, filename=None):
        return take_screenshot(self.driver, filename)
    
    # ============================================
    # Check login validation
    # ============================================

    def check_validation_error(self, email_input_locator, password_input_locator, timeout=SHORT_TIMEOUT):
        """
        Kiểm tra validation error "Please fill out this field" bằng HTML5 Validation API
        """
        try:
            email_input = self.find_element(email_input_locator, timeout=timeout)
            password_input = self.find_element(password_input_locator, timeout=timeout)
            
            # Kiểm tra valueMissing - property chính xác cho "Please fill out this field"
            email_missing = self.driver.execute_script("return arguments[0].validity.valueMissing;", email_input)
            password_missing = self.driver.execute_script("return arguments[0].validity.valueMissing;", password_input)
            
            if email_missing or password_missing:
                return True
            
            # Fallback: Kiểm tra invalid state
            email_invalid = self.driver.execute_script("return arguments[0].validity.valid === false;", email_input)
            password_invalid = self.driver.execute_script("return arguments[0].validity.valid === false;", password_input)
            
            return email_invalid or password_invalid
        except:
            return False