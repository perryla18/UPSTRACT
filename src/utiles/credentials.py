from dotenv import load_dotenv
import os
from src.utiles.contants import VALID_PASSWORD, VALID_USERNAME, INVALID_PASSWORD, INVALID_USER

load_dotenv()

def get_username():
    """
    Lấy username từ environment variable hoặc fallback value
    
    Returns:
        str: Username để đăng nhập
    """
    # Ưu tiên đọc từ .env (REAL value)
    # Nếu không có thì dùng fallback từ constants.py (TEST value)

    return os.getenv('UPSTRACT_USERNAME', VALID_USERNAME)

def get_password():
    return os.getenv('UPSTRACT_PASSWORD', VALID_PASSWORD)

def get_credentials():
    """
    Lấy cả username và password dưới dạng tuple
    
    Returns:
        tuple: (username, password)
    """
    return (get_username(), get_password())

def get_invalid_username():
    return os.getenv('INVALID_USERNAME', INVALID_USER)

def get_invalid_pw():
    return os.getenv('INVALID_PW', INVALID_PASSWORD)

def get_invalid_credentials():
    return (get_invalid_username(), get_invalid_pw())

def validate_credential(username = None, password = None):
    if username is None:
        username = get_username()
    if password is None:
        password = get_password()
    
    return bool(username and password and username.strip())