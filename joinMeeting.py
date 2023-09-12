from selenium import webdriver
import pyautogui as py
import time
 
passcode = "chP8AB"
meet_code = "82761781893"
 
def join(meet, password):
    driver = webdriver.Edge()
    driver.get('https://zoom.us/join')
      
 
    time.sleep(5) #to let the webpage open completely
 
    driver.find_element("xpath", "//input[@id='join-confno']").send_keys(meet_code)
 
    time.sleep(2)
    driver.find_element("xpath", "//a[@id='btnSubmit']").click()
 
    time.sleep(5)
 
    # enter passcode
    enter_passcode = py.locateCenterOnScreen('passc.png')
    py.moveTo(enter_passcode)
    py.click()
    py.write(passcode)
 
    # join the meeting
    #time.sleep(5)
    #btn = py.locateCenterOnScreen("join.png")
    #py.moveTo(btn)
    #py.click()
 
join(meet_code,passcode)
#print("Test")