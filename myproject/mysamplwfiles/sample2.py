from selenium import webdriver
from allure_commons.types import AttachmentType
import allure
import pytest  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/chromedriver.exe")

driver.get("https://www.google.com")


#allure.attachment_type(driver.get_screenshot_as_png(),name="samplescrnsht",attachment_type=AttachmentType.PNG)