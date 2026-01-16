import os
import time
import random
import string
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.utiles.contants import (
    DEFAULT_TIMEOUT,
    SHORT_TIMEOUT,
    LONG_TIMEOUT,
    SCREENSHOT_DIR,
    MAX_RETRIES,
    RETRY_DELAY
)

# ============================================
# WAIT HELPERS
# ============================================

def wait_for_element(driver, locator, timeout = DEFAULT_TIMEOUT, by = By.XPATH):
    """
    Đợi element xuất hiện trên page
    
    Args:
        driver: WebDriver instance
        locator: Locator string (xpath, id, css, etc.)
        timeout: Timeout in seconds
        by: Locator strategy (By.XPATH, By.ID, By.CSS_SELECTOR, etc.)
    
    Returns:
        WebElement: Element nếu tìm thấy
    
    Raises:
        TimeoutException: Nếu không tìm thấy element trong thời gian timeout
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by,locator)))

def wait_for_element_clickable(driver, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
    """
    Đợi element có thể click được
    
    Args:
        driver: WebDriver instance
        locator: Locator string
        timeout: Timeout in seconds
        by: Locator strategy
    
    Returns:
        WebElement: Element nếu có thể click
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable((by, locator)))

def wait_for_element_visible(driver, locator, timeout = DEFAULT_TIMEOUT, by = By.XPATH):
    """
    Đợi element hiển thị (visible) trên page
    
    Args:
        driver: WebDriver instance
        locator: Locator string
        timeout: Timeout in seconds
        by: Locator strategy
    
    Returns:
        WebElement: Element nếu visible
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located((by,locator)))

def is_element_present(driver, locator, timeout=DEFAULT_TIMEOUT, by = By.XPATH):
    """
    Kiểm tra element có tồn tại trên page không (không cần visible)
    
    Args:
        driver: WebDriver instance
        locator: Locator string
        timeout: Timeout in seconds
        by: Locator strategy
    
    Returns:
        bool: True nếu element tồn tại, False nếu không
    """
    try:
        wait_for_element(driver, locator, timeout, by)
        return True
    except TimeoutException:
        return False
    
# ============================================
# ELEMENT INTERACTION HELPERS
# ============================================

def click_element(driver, locator, timeout = DEFAULT_TIMEOUT, by = By.XPATH):
    """
    Click vào element (đợi element clickable trước)
    
    Args:
        driver: WebDriver instance
        locator: Locator string
        timeout: Timeout in seconds
        by: Locator strategy
    """
    element = wait_for_element_visible(driver, locator, timeout, by)
    element.click()

def sends_key_to_element(driver, locator, text, timeout = LONG_TIMEOUT, by = By.XPATH, clear_first = True):
    """
    Nhập text vào element
    
    Args:
        driver: WebDriver instance
        locator: Locator string
        text: Text cần nhập
        timeout: Timeout in seconds
        by: Locator strategy
        clear_first: Có xóa text cũ trước khi nhập không
    """
        
    element = wait_for_element_visible(driver, locator, timeout, by)
    if clear_first:
        element.clear()
    element.send_keys(text)

def get_element_text(driver,locator,timeout=DEFAULT_TIMEOUT, by=By.XPATH):
    element = wait_for_element_visible(driver, locator, timeout, by)
    return element.text

def get_page_title(driver):
    """
    Lấy title của page hiện tại
    
    Args:
        driver: WebDriver instance
    
    Returns:
        str: Page title
    """
    return driver.title

def get_current_url(driver):
    return driver.current_url

# ============================================
# SCREENSHOT HELPERS
# ============================================

def take_screenshot(driver, filename=None):
    """
    Chụp screenshot và lưu vào thư mục screenshots
    
    Args:
        driver: WebDriver instance
        filename: Tên file (nếu None thì tự động tạo tên)
    
    Returns:
        str: Đường dẫn file screenshot
    """
    # Tạo thư mục screenshots nếu chưa có
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    # Tạo tên file nếu không có
    if filename is None:
        filestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        filename = f'screenshot_{filestamp}.png'

    # Đảm bảo có extension .png
    if not filename.endswith('.png'):
        filename  += '.png'

    # Đường dẫn đầy đủ
    filepath = os.path.join(SCREENSHOT_DIR, filename)

    # Chụp screenshot
    driver.save_screenshot(filepath)

    return filepath

def take_screenshot_on_failure(driver, test_name):
    """
    Chụp screenshot khi test fail (dùng trong try-except)
    
    Args:
        driver: WebDriver instance
        test_name: Tên test case
    
    Returns:
        str: Đường dẫn file screenshot
    """
    timestampt = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    filename = f'{test_name}_failure_{timestampt}.png'
    return take_screenshot(driver, filename)


