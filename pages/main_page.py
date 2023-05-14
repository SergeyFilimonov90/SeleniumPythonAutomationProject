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
from pages.locators import MainPageLocators
from utilities.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe')


   # Constants (Just to know the names and prices)

    PRODUCT_1_TEXT = 'Sauce Labs Backpack'
    PRODUCT_1_PRICE = '$29.99'


    product_1_price = ''

    product_1_text = ''


    def get_products_paragraph_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MainPageLocators.PARAGRAPH)))


    def get_products_1_price(self):
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MainPageLocators.PRICE)))
        MainPage.product_1_price = product1.text
        print(f'Global price:{MainPage.product_1_price}')


    def get_products_1_text(self):
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MainPageLocators.PRODUCT)))
        MainPage.product_1_text = product1.text
        print(f'Global name:{MainPage.product_1_text}')

   #Getters

    def get_product_1_text_main_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MainPageLocators.PRODUCT)))

    def get_product_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MainPageLocators.PRICE)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MainPageLocators.ADD_TO_CART_BUTTON)))


    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MainPageLocators.CART_ICON)))


    #Actions

    def add_to_cart_button_click(self):
        self.get_add_to_cart_button().click()

    def cart_icon_click(self):
        self.get_cart_icon().click()
        print('Click cart icon')


    #Methods

    def select_product_1(self):
        with allure.step('select_product_1'):
            Logger.add_start_step(method='select_product_1')
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/inventory.html')
            self.check_text(self.get_products_paragraph_text(), 'Products')
            self.get_products_1_text()
            self.get_products_1_price()
            self.add_to_cart_button_click()
            self.check_text(self.get_cart_icon(),'1')
            self.cart_icon_click()
            Logger.add_end_step(url=self.driver.current_url, method='select_product_1')




