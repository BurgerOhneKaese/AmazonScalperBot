from lib2to3.pgen2 import driver
from selenium import webdriver
import time

# Global Variables
from selenium.common.exceptions import NoSuchElementException

driverPath = input("Gebe den Pfad vom GeckoDriver ein:")
driver = webdriver.Firefox(executable_path=driverPath)
itemURL = input("Gebe den Link vom Produkt ein: ")
username = input("Gebe deine Email-Adreese ein: ")
password = input("Gebe dein Passwort ein:")


def openAmazonLogin():
    driver.get(itemURL)
    time.sleep(5)
    driver.find_element_by_id('sp-cc-accept').click()
    time.sleep(3)
    driver.find_element_by_id("nav-link-accountList-nav-line-1").click()


def sendLoginDate():
    driver.find_element_by_id("ap_email").send_keys(username)
    driver.find_element_by_id("continue").click()
    driver.find_element_by_id("ap_password").send_keys(password)
    driver.find_element_by_id("signInSubmit").click()
    try:
        if (driver.find_element_by_id("ap-account-fixup-phone-skip-link") != None):
            driver.find_element_by_id("ap-account-fixup-phone-skip-link").click()
    except:
        return


def addCart():
    while True:
        try:
            driver.find_element_by_id("buy-now-button").click()
            buyTheItem()
            return
        except NoSuchElementException:
            driver.refresh()
            time.sleep(3)


def buyTheItem():
    driver.find_element_by_id("submitOrderButtonId").click()
    driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    openAmazonLogin()
    sendLoginDate()
    addCart()

