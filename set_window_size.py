# Based on the user input position of the window                            

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

driver=ChromeOptions()
driver.add_experimental_option("detach",True)

driver=Chrome(driver)
driver.get("https://www.amazon.in/")                                   #LOKESH

Xaxis=int(input("Enter Xaxis"))
Yaxis=int(input("Enter Yaxis"))

driver.set_window_size(Xaxis,Yaxis)

sleep(3)
driver.close()