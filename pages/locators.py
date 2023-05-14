from selenium.webdriver.common.by import By



class LoginPageLocators:
    USER_NAME = (By.XPATH,"//input[@ID='user-name']")
    PASSWORD_FIELD = (By.XPATH,"//input[@ID='password']")
    LOGIN_BUTTON = (By.XPATH,"//input[@value='Login']")


class MainPageLocators:
    PARAGRAPH = (By.XPATH,"//span[@class='title']")
    PRODUCT = (By.XPATH,"//*[@id='item_4_title_link']/div")
    PRICE = (By.XPATH,"//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
    ADD_TO_CART_BUTTON = (By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
    CART_ICON = (By.XPATH,"//div[@id='shopping_cart_container']")

class CartStepOneLocators:
    PARAGRAPH = (By.XPATH,"//span[@class='title']")
    PRODUCT_TEXT = (By.XPATH,"//div[@class='inventory_item_name']")
    PRODUCT_PRICE = (By.XPATH,"//div[@class='inventory_item_price']")
    CHECKOUT_BUTTON = (By.XPATH,"//button[@id='checkout']")


class ClientInformationPageLocators:
    CHECKOUT_PARAGRAPH = (By.XPATH,"//span[@class='title']")
    FIRST_NAME = (By.XPATH,"//input[@id='first-name']")
    LAST_NAME = (By.XPATH,"//input[@id='last-name']")
    POSTAL_CODE = (By.XPATH,"//input[@id='postal-code']")
    CONTINUE_BUTTON = (By.XPATH,"//input[@id='continue']")


class CartStepTwoLocators:
    PARAGRAPH = (By.XPATH,"//span[@class='title']")
    PRODUCT_NAME = (By.XPATH, "//div[@class='inventory_item_name']")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")
    SUBTOTAL_PRICE = (By.XPATH, "//div[@class='summary_subtotal_label']")
    TOTAL_PRICE = (By.XPATH, "//div[@class='summary_info_label summary_total_label']")
    TAX = (By.XPATH, "//div[@class='summary_tax_label']")
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")

class FinishPageLocators:
    THANK_YOU_HEADER = (By.XPATH, "//h2[@class='complete-header']")
    THANK_YOU_TEXT = (By.XPATH, "//div[@class='complete-text']")
    BACK_HOME_BUTTON = (By.XPATH, "//button[@class='btn btn_primary btn_small']")



