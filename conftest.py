from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.chrome.options import Options
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    option = Options()
    option.add_argument("--disable-blink-features=AutomationControlled")
    sleep(3)
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)


