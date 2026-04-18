from selenium.webdriver import Chrome,ChromeOptions
from time import sleep

opts=ChromeOptions()
opts.add_experimental_option("detach",True)
driver=Chrome(opts)

driver.get("https://demowebshop.tricentis.com/")
sleep(3)

driver.maximize_window()
sleep(3)

a=driver.find_elements("tag name","input")
#print(a)
print("No. of Input Tag:",len(a))

b=driver.find_elements("tag name","div")
#print(b)
print("No. of Div Tag:",len(b))

c=driver.find_elements("tag name","button")
#print(c)
print("No. of Button Tag: ",len(c))

d=driver.find_elements("tag name","img")
#print(d)
print("No. of Image Tag :",len(d))

e=driver.find_elements("tag name","p")
#print(e)
print("No. of Para Tag :",len(e))

f=driver.find_elements("tag name","section")
#print(f)
print("No. of Section Tag :",len(f))

g=driver.find_elements("tag name","header")
#print(g)
print("No. of Header Tag :",len(g))

h=driver.find_elements("tag name","footer")
#print(h)
print("No. of Footer Tag :",len(h))

i=driver.find_elements("tag name","span")
#print(i)
print("No. of Span Tag :",len(i))

j=driver.find_elements("tag name","a")
#print(j)
print("No. of Anchor Tag :",len(j))

k=driver.find_elements("tag name","label")
#print(k)
print("No. of Label Tag :",len(k))

driver.close()