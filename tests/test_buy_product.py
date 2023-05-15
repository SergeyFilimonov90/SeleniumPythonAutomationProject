import time
import datetime
from datetime import date
import calendar
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.login_page import Login_page
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.client_information_page import ClientInformationPage
from pages.finish_page import FinishPage
from pages.cart_step_two_page import Cart_final_page
from utilities.logger import Logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




@allure.description('Smoke')
def test_buy_product_1(set_up,set_group):
     options = Options()
     options.add_experimental_option('excludeSwitches',['enable-logging'])#to clear the terminal from all gibberish messages
     driver =  = webdriver.Chrome(ChromeDriverManager().install())

     login = Login_page(driver)
     login.authorization()

     main_page_test = MainPage(driver)
     main_page_test.select_product_1()

     cart_page_test = CartPage(driver)
     cart_page_test.cart_test_product_1()

     client_info_page = ClientInformationPage(driver)
     client_info_page.client_page_test()

     cart_step_two_page = Cart_final_page(driver)
     cart_step_two_page.test_product_1()

     finish_page = FinishPage(driver)
     finish_page.finish()


     print('Finish test 1')








