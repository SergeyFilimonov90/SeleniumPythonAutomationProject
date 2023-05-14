from lib2to3.pgen2 import driver
from telnetlib import EC
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self,driver):

        self.driver = driver

    def get_current_url(self):
        '''Method get current url'''
        get_url = self.driver.current_url
        print('Current url ' + get_url)


    def check_text(self, word, value):
        '''In case you want your case to go on regardless of failrure'''
        value_word = word.text
        try:
            assert value_word == value
            print('Word value test passed')
        except AssertionError:
            print(f'Error! Value: {value_word} didn\'t match the value:{value}')
        print(f'passed word:{word}, result: {value}')

    def assert_text(self, word, value):
        '''The same as (check text) but it doesn't convert the elem value to text'''
        try:
            assert word == value
            print('Word value pass')
        except AssertionError:
            print(F'Word value fail word: {word} result: {value}')
        print(f'passed word:{word}, result: {value}')

    def check_value(self, word, value):
        '''Tesing stops if there is a failure'''
        value_word = word.text
        assert value_word == value
        print(f'Word value {value} test passed')


    def screenshot(self):
        '''Method make screenshot'''
        now_date = datetime.datetime.utcnow().strftime('%Y.%m..%d.%H.%M.%S')
        name_screenshot = 'screenshot' + str(now_date) + '.png'  # setting the proper file name and format
        self.driver.save_screenshot('C:\\Users\\Elgyn\\PycharmProjects\\Selenium Python automation project\\screen\\' + name_screenshot)

    def assert_url(self,result):
        '''Mehtod to assert browers's current url'''
        current_url =  self.driver.current_url
        assert current_url == result, 'Wrong url!'
        print(f'Url test passed current url:{current_url} = expected url {result}')


    def assert_final_cart_price_subtotal(self,price,subtotal):
        '''Method that correctly extracts the subtotal value'''
        subtotal = subtotal[12:]
        print('Pass')
        print(f'Subtotal:{subtotal}')
        assert price == subtotal


