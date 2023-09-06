from selenium import webdriver
import pyautogui as py
import time
 
passcode = "9pX9PT"
meet_code = "272 916 9386"
 
def join(meet, password):
    driver = webdriver.Chrome()
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