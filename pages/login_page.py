import time
import datetime
from datetime import date
import calendar
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.locators import LoginPageLocators
from utilities.logger import Logger



class Login_page(Base):

    url = 'https://www.saucedemo.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((LoginPageLocators.USER_NAME)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((LoginPageLocators.PASSWORD_FIELD)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((LoginPageLocators.LOGIN_BUTTON)))


    #Actions

    def input_user_name(self,user_name):
        self.get_user_name().send_keys(user_name)
        print('Input user_name')

    def input_password(self,password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_login_button(self):
        self.get_login_button().click()
        print('clicking button')

    #Methods

    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name('standard_user')
            self.input_password('secret_sauce')
            self.click_login_button()
            Logger.add_end_step(url=self.driver.current_url,method='authorization')






