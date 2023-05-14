import pytest

from selenium import webdriver


@pytest.fixture(scope='function')
def set_up():
    print('Starting testing')
    #The code below is revelent only when you are working with one specific site
    #driver = webdriver.Chrome(executable_path='C:\\Users\\Elgyn\\PycharmProjects\\resource\\chromedriver.exe',chrome_options=options)
    #url = 'https://www.saucedemo.com'
    #driver.get(url)
    #driver.maximize_window()
    yield
    #driver.quit()
    print('Testing completed')

@pytest.fixture(scope='module')
def set_group():
    print('Enter system')

    yield
    #driver.quit()
    print('Quit system')

