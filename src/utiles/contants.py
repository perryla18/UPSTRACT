# URL CONSTANTS
BASE_URL = "https://upstract.com/"
SIGNUP_LOGIN_URL = "https://upstract.com/login"

# TIMEOUT CONSTANTS
DEFAULT_TIMEOUT = 10
SHORT_TIMEOUT = 5
LONG_TIMEOUT = 30
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20

# BROWSER CONTANTS
HEADLESS = False
BROWSER = 'chrome'
WINDOW_SIZE = '1920,1080'
SCREENSHOT_PATH = 'screenshots/'

# TEST DATA CONSTANTS
# Note: Real credentials should be in .env file
# These are fallback values only - use credentials.py for real values
VALID_USERNAME = 'TEST_USER'
VALID_PASSWORD = 'TEST_PASSWORD'
INVALID_USER = 'INVALID_USER'
INVALID_PASSWORD = 'INVALID_PW'

# Menu Options
MENU_PATH = "//a[@id='burger']"
LOGIN_AND_SIGNUP_OPTION = "//a[normalize-space()='Login / Sign Up']"
HOME_OPTION = "//a[normalize-space()='Home']"
WIRE_OPTION = "//a[normalize-space()='Wire']"
LIGHT_MODE_OPTION = "//a[normalize-space()='Light Mode']"
SEARCH_OPTION = "//a[normalize-space()='Search']"
SETTINGS_DARK_MODE_OPTION = "//a[normalize-space()='Settings & Dark Mode']"
CUSTOMIZE_OPTION = "//a[normalize-space()='Customize News Grid']"
MEMBERSHIP_OPTION = "//a[normalize-space()='Pro Membership']"

# Login| SIGNUP Page
SIGNUP_LOGO = "//h2[normalize-space()='Sign Up Now']"
INPUT_EMAIL = "//form[@action='/signup']//input[@placeholder='Your E-Mail']"
INPUT_PW = "//input[@id='new-password']"
SIGNUP_BUTTON = "//button[@id='btn_signup']"

LOGIN_LOGO = "//h2[normalize-space()='Existing User? Log In']"
INPUT_EMAIL_LOGIN = "//form[@action='/login']//input[@placeholder='Your E-Mail']"
UNPUT_PW_LOGIN = "//input[@id='current-password']"
LOGIN_BUTTON = "//button[@id='btn_login']"

# FILE PATHS
REPORTS_DIR = "reports/"
SCREENSHOT_DIR = "screenshots/"
TEST_DATA_DIR = "src/fixtures/"

# RETRY CONSTANTS
MAX_RETRIES = 3
RETRY_DELAY = 2
