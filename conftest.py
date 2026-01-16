import pytest
from src.utiles.config import get_driver
from src.utiles.contants import IMPLICIT_WAIT

@pytest.fixture(scope="function")
def driver():
    """
    Fixture để tạo và quản lý WebDriver instance
    Tự động khởi tạo và đóng driver sau mỗi test
    """
    driver = get_driver()
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.maximize_window()

    yield driver
    driver.quit()