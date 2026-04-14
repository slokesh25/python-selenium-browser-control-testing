#opening the browser

from selenium.webdriver import Chrome,ChromeOptions
opts=ChromeOptions()
opts.add_experimental_option("detach",True)
c=Chrome(opts)
  
#closeing the browser
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts=ChromeOptions()
opts.add_experimental_option("detach",True)
c=Chrome(opts)  # this line is  opening the browser 
sleep(3)
c.close() # this line is close the current tab
c.quit() # closing the entire browser 
 
# lunching an application 
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts=ChromeOptions()
opts.add_experimental_option("detach",True)
c=Chrome(opts)
c.get("https://www.amazon.in/")
sleep(3)
c.close()

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts=ChromeOptions()
opts.add_experimental_option("detach",True)
print("APPLICATIONS:\n1.Amazon\n2.Fliptkart\n3.Myntra")
app = int(input('Enter Your Choice '))
if app == 1:
    c=Chrome(opts)
    c.get("https://www.amazon.in/")
elif app == 2:
    c=Chrome(opts)
    c.get("https://www.flipkart.com/")
elif app == 3:
    c=Chrome(opts)
    c.get("https://www.myntra.com/")
else:
    print("Invilad Choice")
  
# maximize the window 
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
drive=ChromeOptions()
drive=Chrome(drive)
drive.get("https://www.amazon.in/")
sleep(3)
drive.maximize_window()
sleep(3)

#minimize the window
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
drive=ChromeOptions()
drive=Chrome(drive)
drive.get("https://www.amazon.in/")
sleep(3)
drive.minimize_window()
sleep(3)

# minmize and maximize the window
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
drive=ChromeOptions()
drive.add_experimental_option("detach",True)
drive=Chrome(drive)
drive.get("https://www.amazon.in/")
sleep(3)
drive.minimize_window()
sleep(3)
drive.maximize_window()
sleep(3) 

# Full screen the window 
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
drive=ChromeOptions()
drive.add_experimental_option("detach",True)
drive=Chrome(drive)
drive.get("https://www.amazon.in/")
sleep(3)
drive.fullscreen_window()
sleep(3)

# Back screen one screen to back another screen 
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
# sleep(3)

# To launch amazon.in after 3 seconds minimize the vindow
# and after 3s maximize and after 3s launch flipkart and after
# 5s click on back and, after 2s click on forvard and after 2s
# refersh the browser and after 3s close the brouser
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
drive=ChromeOptions()
drive.add_experimental_option("detach",True)
drive=Chrome(drive)
drive.get("https://www.amazon.in/")
sleep(3)
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
drive.quit()

