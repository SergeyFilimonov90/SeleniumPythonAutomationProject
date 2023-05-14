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
from pages.locators import FinishPageLocators
from utilities.logger import Logger



class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Getters

    def get_thank_you_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinishPageLocators.THANK_YOU_HEADER)))


    def get_thank_you_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinishPageLocators.THANK_YOU_TEXT)))


    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((FinishPageLocators.BACK_HOME_BUTTON )))



    #Methods

    def click_finish_button(self):
        self.get_finish_button().click()


    def finish(self):
        with allure.step('finish'):
            Logger.add_start_step(method='finish')
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/checkout-complete.html')
            self.check_value(self.get_thank_you_header(),'Thank you for your order!')
            self.check_value(self.get_thank_you_text(),'Your order has been dispatched, and will arrive just as fast as the pony can get there!')
            self.click_finish_button()
            self.assert_url('https://www.saucedemo.com/inventory.html')
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='finish')




