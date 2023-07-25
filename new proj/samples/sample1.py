




     from selenium import webdriver
     import  time
     from selenium.webdriver.common.by import By

      from PIL import Image
      from selenium.webdriver.common.keys import Keys

      driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
      time.sleep(2)
      driver.maximize_window()
driver.get("http://localhost:80")
time.sleep(2)
driver.save_screenshot("landing.png")
pgtxt=driver.find_element(By.XPATH,'//*[@id="main-navbar-collapse"]/ul[2]/li[1]/a')
x=pgtxt.text

if (x=="Login"):
   print("Login is successful")
else:
   print("Unable to login")

wlcmtxt=driver.find_element(By.XPATH,'//*[@class="jumbotron text-center"]/h1').text
if (wlcmtxt=="Welcome"):
   print("welcome text exists")
else:
   print("welcome text doesnot exist")

pgtxt.click()
time.sleep(5)
#  login
usrnme=driver.find_element(By.XPATH,'//*[@id="LoginInput_UserNameOrEmailAddress"]')
usrnme.send_keys("admin")
time.sleep(2)
pwd=driver.find_element(By.XPATH,'//*[@id="LoginInput_Password"]')
pwd.send_keys("1q2w3E")
time.sleep(2)

#Click login button
lgnbtn=driver.find_element(By.XPATH,'//*[@name="Action"]')
lgnbtn.click()
time.sleep(5)


errmsg=driver.find_element(By.XPATH,'//*[@id="AbpPageAlerts"]/div').text
#scfllgn=driver.find_element(By.XPATH,'')
if (errmsg=="Invalid username or password!"):
   print("required error msg displayed")
elif :
   print("error msg did not displayed")

   time.sleep(2)
   driver.save_screenshot("error msg.png")

SiteLogin()