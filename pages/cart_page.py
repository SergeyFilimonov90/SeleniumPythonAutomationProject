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
from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.locators import CartStepOneLocators
from utilities.logger import Logger


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Getters

    def get_product_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepOneLocators.PRODUCT_TEXT)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepOneLocators.PRODUCT_PRICE)))


    def get_paragraph_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepOneLocators.PARAGRAPH)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepOneLocators.CHECKOUT_BUTTON)))



    def get_products_price_1_cart(self):
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepOneLocators.PRODUCT_PRICE)))
        product1_price_cart = product1.text
        print(f'cart page price: {product1_price_cart}')
        return product1_price_cart

    def get_products_text_1_cart(self):
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepOneLocators.PRODUCT_TEXT)))
        product1_text_cart = product1.text
        print(f'cart page text: {product1_text_cart}')
        return product1_text_cart

    #Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Item added to cart')

    #Methods

    def cart_test_product_1(self):
        with allure.step('cart_test_product_1'):
            Logger.add_start_step(method='select_product_1')
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/cart.html')
            self.get_products_text_1_cart()
            self.get_products_price_1_cart()
            self.assert_text(MainPage.product_1_text, self.get_products_text_1_cart())
            self.assert_text(MainPage.product_1_price,self.get_products_price_1_cart())
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method='select_product_1')





