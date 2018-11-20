from selenium.webdriver.common.by import By
from POMDemo.Locators.LoginPageLocators import LoginPageLocators



class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, LoginPageLocators.username_textbox_id).clear()
        self.driver.find_element(By.ID, LoginPageLocators.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, LoginPageLocators.password_textbox_id).clear()
        self.driver.find_element(By.ID, LoginPageLocators.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, LoginPageLocators.login_button_id).click()


