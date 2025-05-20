from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    productpage = ProductPage(browser)
    productpage.check_title('Samsung galaxy s6')

    # browser.get('https://demoblaze.com/')
    # galaxy_s6 = browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    # galaxy_s6.click()
    # title = browser.find_element(By.CSS_SELECTOR, 'h2')
    # assert title.text == 'Samsung galaxy s6'

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor_link()
    time.sleep(2) #!--
    homepage.check_goods_count(2)

    # browser.get('https://demoblaze.com/')
    # monitor_link = browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    # monitor_link.click()
    # time.sleep(2) #!--
    # monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    # assert len(monitors) == 2
