import time
import datetime
from datetime import date
import calendar
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import datetime
from datetime import date
import calendar
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from pages.main_page import MainPage
from pages.locators import CartStepTwoLocators
from utilities.logger import Logger



class Cart_final_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def get_checkout_overview_paragraph_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.PARAGRAPH )))


    def get_product_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.PRODUCT_NAME)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.PRODUCT_PRICE)))

    def get_subtotal_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.SUBTOTAL_PRICE)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.FINISH_BUTTON)))

    def get_tax(self):
        tax = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.TAX)))
        tax_text = tax.text[6:]
        print(tax_text)
        return tax_text


    def get_total(self):
        total = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.TOTAL_PRICE)))
        total_text = total.text[8:]
        return total_text

    def get_products_price_subtotal_numeric(self):
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.SUBTOTAL_PRICE)))
        product_subtotal_price_numeric = product1.text[13:]
        print(f'Subtotal: {product_subtotal_price_numeric}')
        return product_subtotal_price_numeric



    def get_products_name_cart(self):
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.PRODUCT_NAME)))
        product_name = product1.text
        print(f'Product name: {product_name}')
        return product_name


    def get_products_price_cart(self):
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.PRODUCT_PRICE)))
        product_price = product1.text
        print(f'Price: {product_price}')
        return product_price

    def get_products_pricesubtotal_cart(self):
        product1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((CartStepTwoLocators.SUBTOTAL_PRICE)))
        product_subtotal_price = product1.text[12:]
        print(f'Subtotal: {product_subtotal_price}')
        return product_subtotal_price


    #Actions

    def click_final_finish_button(self):
        self.get_finish_button().click()
        print('Click finish button')

    #Methods

    def test_product_1(self):
        Logger.add_start_step(method='test_product_1')
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-step-two.html')
        self.check_text(self.get_checkout_overview_paragraph_text(), 'Checkout: Overview')
        self.get_products_name_cart()
        self.get_products_price_cart()
        self.get_products_pricesubtotal_cart()
        self.assert_text(MainPage.product_1_text, self.get_products_name_cart())
        self.assert_text(MainPage.product_1_price, self.get_products_price_cart())
        self.assert_text(MainPage.product_1_price,self.get_products_pricesubtotal_cart())
        self.click_final_finish_button()
        Logger.add_end_step(url=self.driver.current_url, method='test_product_1')








