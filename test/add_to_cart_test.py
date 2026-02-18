import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page.base_page import BasePage
from page.add_to_cart_page import CartPage



def test_add_to_cart(driver):
    home = HomePage(driver)
    cart = CartPage(driver)

