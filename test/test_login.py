from selenium.webdriver.common.by import By
import time
from pages.home_page import HomePage
from pages.login_form import LoginForm
from pages.product_page import ProductPage
from selenium.webdriver.common.keys import Keys

def test_login(browser):
    homepage = HomePage(browser)
    loginform = LoginForm(browser)

    homepage.open()
    loginform.open_login_form()

    loginform.fill_login()
    loginform.fill_password()

    loginform.click_login_button()
    loginform.check_auth()

def test_logout_not_exist(browser):
    homepage = HomePage(browser)
    homepage.open()
    logout = browser.find_element(By.ID, 'logout2')
    assert not logout.is_displayed()
