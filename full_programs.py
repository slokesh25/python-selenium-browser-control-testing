# #opening the browser

# from selenium.webdriver import Chrome,ChromeOptions
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# c=Chrome(opts)
  
# #closeing the browser

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# c=Chrome(opts)  # this line is  opening the browser 
# sleep(3)
# c.close() # this line is close the current tab
# c.quit() # closing the entire browser 
 
# # lunching an application 

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# c=Chrome(opts)
# c.get("https://www.amazon.in/")
# sleep(3)
# c.close()

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# print("APPLICATIONS:\n1.Amazon\n2.Fliptkart\n3.Myntra")
# app = int(input('Enter Your Choice '))
# if app == 1:
#     c=Chrome(opts)
#     c.get("https://www.amazon.in/")
# elif app == 2:
#     c=Chrome(opts)
#     c.get("https://www.flipkart.com/")
# elif app == 3:
#     c=Chrome(opts)
#     c.get("https://www.myntra.com/")
# else:
#     print("Invilad Choice")
  
# # maximize the window 

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# drive=ChromeOptions()
# drive=Chrome(drive)
# drive.get("https://www.amazon.in/")
# sleep(3)
# drive.maximize_window()
# sleep(3)

# #minimize the window

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# drive=ChromeOptions()
# drive=Chrome(drive)
# drive.get("https://www.amazon.in/")
# sleep(3)
# drive.minimize_window()
# sleep(3)

# # minmize and maximize the window

# driver=ChromeOptions()
# driver.add_experimental_option("detach",True)

# driver=Chrome(driver)
# driver.get("https://www.amazon.in/")

# width=int(input("Enter width"))
# height=int(input("Enter height"))

# driver.set_window_size(width,height)

# sleep(3)
# driver.close()

# Based on the user input position of the window

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# driver=ChromeOptions()
# driver.add_experimental_option("detach",True)

# driver=Chrome(driver)
# driver.get("https://www.amazon.in/")

# Xaxis=int(input("Enter Xaxis"))
# Yaxis=int(input("Enter Yaxis"))

# driver.set_window_size(Xaxis,Yaxis)

# sleep(3)
# driver.close()

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# drive=ChromeOptions()
# drive.add_experimental_option("detach",True)
# drive=Chrome(drive)
# drive.get("https://www.amazon.in/")
# sleep(3)
# drive.minimize_window()
# sleep(3)
# drive.maximize_window()
# sleep(3) 

# # Full screen the window 

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# drive=ChromeOptions()
# drive.add_experimental_option("detach",True)
# drive=Chrome(drive)
# drive.get("https://www.amazon.in/")
# sleep(3)
# drive.fullscreen_window()
# sleep(3)

#  main screen to back screen 

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# drive=ChromeOptions()
# drive.add_experimental_option("detach",True)
# drive=Chrome(drive)
# drive.get("https://www.amazon.in/")
# sleep(3)
# drive.get("https://www.myntra.com/")
# sleep(3)
# drive.back()
# # sleep(3)

# To launch amazon.in after 3 seconds minimize the window

# and after 3s maximize and after 3s launch flipkart and after
# 5s click on back and, after 2s click on forvard and after 2s
# refersh the browser and after 3s close the brouser
# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# drive=ChromeOptions()
# drive.add_experimental_option("detach",True)
# drive=Chrome(drive)
# drive.get("https://www.amazon.in/")
# sleep(3)
# drive.maximize_window()
# sleep(3)
# drive.get("https://www.flipkart.com/")
# sleep(5)
# drive.back()
# sleep(2)
# drive.forward()
# sleep(2)
# drive.refresh()
# sleep(3)
# drive.quit()

# This code is for [get] the size of the window and position of the window

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# driver=ChromeOptions()
# driver.add_experimental_option("detach",True)
# driver=Chrome(driver)
# driver.get("https://www.amazon.in/")
# sleep(3)
# size=driver.get_window_size()
# print("size",size)
# position=driver.get_window_position()
# print("position",position)

# size_position= driver.get_window_rect()
# print("size_position",size_position)
# driver.close()
 
# [set] the window size and positions and rect also
# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# driver=ChromeOptions()
# driver.add_experimental_option("detach",True)
# driver=Chrome(driver)
# driver.get("https://www.amazon.in/")
# driver.set_window_size(500,250)
# sleep(3)
# driver.set_window_position(250,250)
# sleep(3)
# driver.set_window_rect(400,400,100,100)
# sleep(3)
# driver.close()

# Based on the user input for window size

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep

# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)

# driver=Chrome(opts)
# driver.get("https://www.spacex.com/")
# sleep(3)

# width=int(input('Enter width'))
# height=int(input('Enter height'))

# driver.set_window_size(width,height)
# sleep(3)
# driver.close()
 
# Based on the user input for window position size 

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep

# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)

# driver=Chrome(opts)
# driver.get("https://www.spacex.com/")
# sleep(3)

# Xaxis=int(input('Enter Xaxis'))
# Yaxis=int(input('Enter Yaxis'))

# driver.set_window_position(Xaxis,Yaxis)
# sleep(3)
# driver.close()

 
# get the title of the webpage 

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://www.spacex.com/")
# # driver.get("https://www.amazon.in/")
# sleep(3)
# driver.maximize_window()
# title=driver.title
# print("title:",title)
# driver.close()
  
# get the current utl of the webpage 

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://www.spacex.com/")
# sleep(3)
# url=driver.current_url
# print("url:",url)
# driver.close()

# get the source from the page source 
# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://www.spacex.com/")
# sleep(3)
# source=driver.page_source
# print("source",source)
# driver.close()

# method 1 for id selector 

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(3)
# search_tf=driver.find_element("id","twotabsearchtextbox")
# search_tf.send_keys("mobiles")
# sleep(3)
# search_btn=driver.find_element("id","nav-search-submit-button")
# search_btn.click()

# # method 2 for id selector

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(3)
# driver.find_element("id","twotabsearchtextbox").send_keys("mobiles")
# sleep(2)
# driver.find_element("id","nav-search-submit-button").click()

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# sleep(3)
# driver.find_element("class name","oxd-input.oxd-input--active").send_keys("loki2545")
# sleep(3)
# driver.find_element("class name","oxd-input.oxd-input--active").send_keys("lokesh")
# sleep(3)
# driver.close()

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://testautomationpractice.blogspot.com/")
# sleep(3)
# driver.find_element("class name","form-control").send_keys("lokesh")
# sleep(3)
# driver.find_element("class name","form-control").send_keys("lokesh@gmail")


#find the text locator 
# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://www.instagram.com/#")
# sleep(3)
# driver.find_element("link text","Forgot password?").click()
# sleep(3)
# driver.close()

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://www.saucedemo.com/")
# sleep(3)
# driver.find_element("id","user-name").send_keys("lokesh")
# sleep(3)
# driver.find_element("id","password").send_keys("loki123")
# sleep(3)
# This line login button is not click because login name is attribute
# it's not center of the tag <input>login</input> like this so it's not execute
# driver.find_element("link text","Login").click()
# sleep(3)

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://www.amazon.in/")
# sleep(3)
# driver.maximize_window()
# driver.find_element("partial link text","Sell").click()
# sleep(3)

# # css selector
# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://testautomationpractice.blogspot.com/")
# sleep(3)
# driver.find_element("css selector","input[placeholder='Enter EMail']").send_keys("lokesh@gmail.com")
# driver.find_element("css selector","input[value=sunday]").click()
# sleep(3)
# driver.find_element("css selector","input[value=monday]").click()
# sleep(3)
# driver.find_element("css selector","input[value=tuesday]").click()
# sleep(3)
# driver.find_element("css selector","input[value=wednesday]").click()
# sleep(3)
# driver.find_element("css selector","input[value=thursday]").click()
# sleep(3)


# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# sleep(3)
# driver.find_element("class name","ico-register").click()
# sleep(3)
# driver.find_element("css selector","input[value='M']").click()
# sleep(3)
# driver.find_element("css selector","input[class='text-box single-line']").send_keys("lokesh")
# sleep(3)
# driver.find_element("css selector","input[class='text-box single-line']").send_keys("sathiyam")
# sleep(3)

# tag name locator

# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# opts=ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=Chrome(opts)

# driver.get("https://demowebshop.tricentis.com/")
# sleep(3)

# driver.maximize_window()
# sleep(3)

# a=driver.find_elements("tag name","input")
# #print(a)
# print("No. of Input Tag:",len(a))

# b=driver.find_elements("tag name","div")
# #print(b)
# print("No. of Div Tag:",len(b))

# c=driver.find_elements("tag name","button")
# #print(c)
# print("No. of Button Tag: ",len(c))

# d=driver.find_elements("tag name","img")
# #print(d)
# print("No. of Image Tag :",len(d))

# e=driver.find_elements("tag name","p")
# #print(e)
# print("No. of Para Tag :",len(e))

# f=driver.find_elements("tag name","section")
# #print(f)
# print("No. of Section Tag :",len(f))

# g=driver.find_elements("tag name","header")
# #print(g)
# print("No. of Header Tag :",len(g))

# h=driver.find_elements("tag name","footer")
# #print(h)
# print("No. of Footer Tag :",len(h))

# i=driver.find_elements("tag name","span")
# #print(i)
# print("No. of Span Tag :",len(i))

# j=driver.find_elements("tag name","a")
# #print(j)
# print("No. of Anchor Tag :",len(j))

# k=driver.find_elements("tag name","label")
# #print(k)
# print("No. of Label Tag :",len(k))

# driver.close()

# xpath absolute

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)

driver=Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")

driver.maximize_window()
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
sleep(3)

# sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[2]/input").send_keys("lokesh")
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[3]/input").send_keys("sathiyam")
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[4]/input").send_keys("risha@gmail.com")
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[1]/input").send_keys("loki123")
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[2]/input").send_keys("loki123")
sleep(3)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[4]/input").click()
sleep(3) 

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[1]/div[1]/input").click()
sleep(3)
