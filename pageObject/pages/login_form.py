import time
from pageObject.entity.user import User
from selenium.webdriver.common.by import By


class LoginForm:

    def __init__(self, browser):
        self.browser = browser

    def open_login_form(self):
        self.browser.find_element(By.ID, 'login2').click()
        assert self.browser.find_element(By.ID, "signInModalLabel")

    def fill_login(self, username):
        login = self.browser.find_element(By.ID, 'loginusername')
        login.send_keys(username)

    def fill_password(self,userpassword):
        password = self.browser.find_element(By.ID, 'loginpassword')
        password.send_keys(userpassword)

    def click_login_button(self):
        self.browser.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
        time.sleep(3)  # !--


    def check_auth(self, usernamelogin):
        username = self.browser.find_element(By.ID, 'nameofuser')
        assert username.text == 'Welcome ' + usernamelogin

