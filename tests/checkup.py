# this module is for running some block of code for checkup purposes

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

chrome_driver_service = Service("C:/Program Files/Google/Chrome/Application/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_service, options=chrome_options)

driver.get("")

sleep(2)