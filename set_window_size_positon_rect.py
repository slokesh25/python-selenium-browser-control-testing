# [set] the window size and positions and rect also

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

driver=ChromeOptions()
driver.add_experimental_option("detach",True)

driver=Chrome(driver)
driver.get("https://www.amazon.in/")                              
driver.set_window_size(500,250)
sleep(3)

driver.set_window_position(250,250)
sleep(3)

driver.set_window_rect(400,400,100,100)
sleep(3)

driver.close()