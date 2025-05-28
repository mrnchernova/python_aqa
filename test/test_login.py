from selenium.webdriver.common.by import By
from pageObject.pages.home_page import HomePage
from pageObject.pages.login_form import LoginForm
from pageObject.entity.user import User
import time


def test_login(browser):
    user = User('Hello900', 'Obama')
    homepage = HomePage(browser)
    loginform = LoginForm(browser)

    homepage.open()
    loginform.open_login_form()

    loginform.fill_login(user.username)
    loginform.fill_password(user.password)

    loginform.click_login_button()
    time.sleep(3)  # !--
    loginform.check_auth(user.username)

def test_logout_not_exist(browser):
    homepage = HomePage(browser)
    homepage.open()
    logout = browser.find_element(By.ID, 'logout2')
    assert not logout.is_displayed()
