#  main screen to back screen 

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

drive=ChromeOptions()
drive.add_experimental_option("detach",True)

drive=Chrome(drive)
drive.get("https://www.amazon.in/")
sleep(3)

drive.get("https://www.myntra.com/")
sleep(3)

drive.back()
sleep(3)