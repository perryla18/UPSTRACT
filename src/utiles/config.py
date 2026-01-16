from src.utiles.contants import HEADLESS, BROWSER, WINDOW_SIZE, DEFAULT_TIMEOUT, SHORT_TIMEOUT, LONG_TIMEOUT, EXPLICIT_WAIT, IMPLICIT_WAIT
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.edge.options import Options as EdgeOption
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

def get_browser_options():
    """
    Tạo và cấu hình browser options dựa trên BROWSER và HEADLESS constants
    
    Returns:
        options: Browser options object (ChromeOptions, FirefoxOptions, hoặc EdgeOptions)
    """

    if BROWSER.lower() == 'chrome':
        options = ChromeOption()

        # Headless:
        if HEADLESS:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        
        # Windowsize
        if WINDOW_SIZE:
            options.add_argument(f'--window-size={WINDOW_SIZE}')
        else:
            options.add_argument('--start-maximized')

        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        return options  # Thêm return ở đây
    
    elif BROWSER.lower() == 'edge':
        options = EdgeOption()

        if HEADLESS:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        
        # Windowsize
        if WINDOW_SIZE:
            options.add_argument(f'--window-size={WINDOW_SIZE}')
        else:
            options.add_argument('--start-maximized')

        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        return options

    else:
        raise ValueError(f'{BROWSER} is not supported')
    

def get_driver():
    """
    Tạo và trả về WebDriver instance với cấu hình từ constants
    
    Returns:
        driver: WebDriver instance (Chrome, Firefox, hoặc Edge)
    """
    options = get_browser_options()
    if BROWSER.lower() == 'chrome':
        driver_path = ChromeDriverManager().install()
        if 'THIRD_PARTY_NOTICES' in driver_path:
            # Tìm file chromedriver trong cùng thư mục
            driver_dir = os.path.dirname(driver_path)
            driver_path = os.path.join(driver_dir, 'chromedriver')
        
        if os.path.exists(driver_path):
            os.chmod(driver_path, 0o755)
        
        service = ChromeService(driver_path)
        driver = webdriver.Chrome(service=service, options=options)

    elif BROWSER.lower() == 'edge':
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
    
    else:
        raise ValueError(f'Browser {BROWSER} is not supported')

    
    # Cấu hình driver trước khi return
    driver.implicitly_wait(IMPLICIT_WAIT)
    if not HEADLESS and not WINDOW_SIZE:
        driver.maximize_window()
    
    return driver