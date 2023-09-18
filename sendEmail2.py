from selenium import webdriver
import pyautogui as py
import time
from emailMessages import *

def sendEmail():
    driver = webdriver.Firefox()
    driver.get("https://gmail.com")

    time.sleep(5)

    driver.find_element("xpath", '//*[@id ="identifierId"]').send_keys("mperez568923@gmail.com")
    driver.find_element("xpath", '//*[@id ="identifierNext"]').click()

sendEmail()