from xmlrpc.client import boolean

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from PIL import Image
import openpyxl
import xlrd
drvr = webdriver.Chrome(executable_path="C:\chromedriver.exe")
drvr.get("http://localhost:80")
#time.sleep(2)
drvr.maximize_window()
#time.sleep(2)
lgnbtn = drvr.find_element(By.XPATH, '//*[@class="px-4 btn btn-primary"]')
lgnbtn.click()

lgs = ["admin9", "admin1", "admin"]
for usr in range(len(lgs)):
    print(len(lgs))
    print(lgs[usr])
    usrnme = drvr.find_element(By.XPATH, '//*[@id="LoginInput_UserNameOrEmailAddress"]')
    usrnme.send_keys(lgs[usr])
    #time.sleep(2)
    pwdtxt = drvr.find_element(By.XPATH, '//*[@id="LoginInput_Password"]')
    pwdtxt.send_keys("1q2w3E*")
    #time.sleep(2)
    fnllgn = drvr.find_element(By.XPATH, '//*[@class="d-grid gap-2"]/button')
    fnllgn.click()
    #time.sleep(2)
    # ermsgg=drvr.find_element(By.XPATH,'//*[@id="AbpPageAlerts"]/div')
    # print(ermsgg.text)
    if lgs[usr]=="admin":
        print("correct user name is entered")
        lgnagn = drvr.find_element(By.XPATH, '//*[@id="main-navbar-collapse"]/ul[2]/li[1]/a')
        lgnagn.click()
        #time.sleep(5)
       # break
    else:
           if drvr.find_element(By.XPATH, '//*[@id="AbpPageAlerts"]/div').is_displayed():
              lgnagn = drvr.find_element(By.XPATH, '//*[@id="main-navbar-collapse"]/ul[2]/li[1]/a')
              lgnagn.click()
             # time.sleep(5)
           else:
              # lgnbtn=drvr.find_element(By.XPATH,'//*[@class="px-4 btn btn-primary"]')
              # lgnbtn.click()
                lgnagn = drvr.find_element(By.XPATH, '//*[@id="main-navbar-collapse"]/ul[2]/li[1]/a')
                lgnagn.click()
                usr = usr + 1
                continue
