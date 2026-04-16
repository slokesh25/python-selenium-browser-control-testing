# To launch amazon.in after 3 seconds minimize the window                
# and after 3s maximize and after 3s launch flipkart and after
# 5s click on back and, after 2s click on forvard and after 2s
# refersh the browser and after 3s close the brouser

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

drive=ChromeOptions()
drive.add_experimental_option("detach",True)

drive=Chrome(drive)
drive.get("https://www.amazon.in/")                                

drive.maximize_window()
sleep(3)

drive.get("https://www.flipkart.com/")
sleep(5)

drive.back()
sleep(2)

drive.forward()
sleep(2)

drive.refresh()
sleep(3)

drive.quit()                                                        #LOKESH
sleep(3)