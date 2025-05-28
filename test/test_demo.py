import time
from pageObject.pages.home_page import HomePage
from pageObject.pages.product_page import ProductPage


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    productpage = ProductPage(browser)
    productpage.check_title('Samsung galaxy s6')

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor_link()
    time.sleep(2) #!--
    homepage.check_goods_count(2)