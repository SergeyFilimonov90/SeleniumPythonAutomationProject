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
from pages.locators  import ClientInformationPageLocators
from utilities.logger import Logger


class ClientInformationPage(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Getters

    def get_first_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((ClientInformationPageLocators.FIRST_NAME)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((ClientInformationPageLocators.LAST_NAME)))

    def get_posta_code_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((ClientInformationPageLocators.POSTAL_CODE)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((ClientInformationPageLocators.CONTINUE_BUTTON)))

    def get_client_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((ClientInformationPageLocators.CHECKOUT_PARAGRAPH)))


    #Actions

    def input_first_name(self,first_name):
        self.get_first_name_field().send_keys(first_name)
        print('Input first_name')

    def input_last_name(self,last_name):
        self.get_last_name_field().send_keys(last_name)
        print('Input last_name')

    def input_postal_code(self,postal_code):
        self.get_posta_code_field().send_keys(postal_code)
        print('Input postal code')

    def click_continue(self):
        self.get_continue_button().click()
        print('clicking continue button')

    #Methods

    def client_page_test(self):
        with allure.step('client_page_test'):
            Logger.add_start_step(method='client_page_test')
            self.check_text(self.get_client_text(),'Checkout: Your Information')
            self.input_first_name('Frank')
            self.input_last_name('Elgyn')
            self.input_postal_code('14546256')
            self.click_continue()
            Logger.add_end_step(url=self.driver.current_url, method='client_page_test')





