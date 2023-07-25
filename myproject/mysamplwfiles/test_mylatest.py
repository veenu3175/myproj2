from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.chrome(executable_path='C:/chromedriver.exe')

driver.get("https://localhost:80")