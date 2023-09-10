#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install request')


# In[3]:


import selenium 
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import re 
import requests


# In[4]:


import time
from time import sleep


# In[5]:


driver=webdriver.Chrome()


# # Question:1

# In[ ]:


driver=webdriver.Chrome()


# In[6]:


driver.get("https://www.amazon.in")


# In[7]:


driver.maximize_window()


# In[16]:


input_search=driver.find_element(By.ID,"twotabsearchtextbox")


# In[17]:


search_button=driver.find_element(By.ID,"nav-search-submit-text")
                                            
input_search.send_keys("guitar")
search_button.click()                                            


# In[84]:


product=[]
price=[]
pop=driver.find_elements(By.XPATH,'//span[@class="a-price"]')
for j in pop:
    price.append(j.text)
    
tit=driver.find_elements(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]')

for p in tit:
    product.append(p.text)
x=product[0:64]
data=({"product_name":x,"Product_price":price})
df=pd.DataFrame(data)
df


# # Question:2

# In[ ]:


driver=webdriver.Chrome()


# In[6]:


driver.get("https://www.amazon.in")


# In[7]:


input_search=driver.find_element(By.ID,"twotabsearchtextbox")


# In[8]:


search_button=driver.find_element(By.ID,"nav-search-submit-text")


# In[9]:


product_name=input("enter product name ")
input_search.send_keys(product_name)
search_button.click()                                            


# In[43]:


brand=[]
for i in range(0,3):
    l=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
    for d in l:
        brand.append(d.text)
    n_b=driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[22]/div/div/span/a[3]')
    #n_b.click()
    time.sleep(3)
im=[]
for i in range(0,3):
    I=driver.find_elements(By.CLASS_NAME,"s-image")
    for i in I:
        im.append(i)
rate=[]
for i in range(0,3):
    u=driver.find_elements(By.CLASS_NAME,"a-price-whole")
    for i in u:
        rate.append(i.text)
k=[]
for i in range(0,3):
    o=driver.find_elements(By.XPATH,'//span[@class="a-color-base a-text-bold"]')

    for i in o:
        k.append(i.text)
        
data=({"Brand_name_with_color":brand,"Product_price":rate,"Product_image":im,"Delivere_date":k})
df=pd.DataFrame(data)
df
    


# In[45]:


df.to_csv("applemobile.csv")


# # Question:4

# In[64]:


driver=webdriver.Chrome()


# In[65]:


driver.get("https://www.flipkart.com")


# In[66]:


input_search=driver.find_element(By.XPATH,'//input[@name="q"]')


# In[67]:


button=driver.find_element(By.XPATH,'//button[@class="_2iLD__"]')


# In[68]:


input_search.send_keys("smartphon")
button.click()                                            


# In[ ]:


Feature=[]
G=driver.find_elements(By.XPATH,'//div[@class="fMghEO"]')
for i in G:
    t=(i.text)
    Feature.append(t)
brand=[]
b=driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
for i in b:
    brand.append(i.text)
p=[]
l=driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]')

for i in l:
    p.append(i.text)   
i=[]
I=driver.find_elements(By.XPATH,'//div[@class="_2QcLo-"]')
for r in I:
    i.append(r) 
    
URL=[]
url=driver.find_elements(By.XPATH,'//a[@class="_1fQZEK"]')
for i in url:
    URL.append(i.get_attribute('href'))
    
data=({"Brand_Name":brand,'Brand_Feature':Feature,"Product_price":p,"Product_image":i,"Product_URL":URL})
df=pd.DataFrame(data)


# In[ ]:


df.to_csv("smartphon.csv")


# # Question:6

# In[62]:


driver=webdriver.Chrome()


# In[63]:


driver.get("https://www.digit.in")


# In[64]:


driver.find_elements(By.XPATH,'/html/body/div[2]/div/ul/li[5]/span')[0].click()


# In[65]:


driver.find_elements(By.XPATH,'/html/body/div[2]/div/ul/li[5]/div[2]/div/div[2]/div/ul[2]/li[2]/a')[0].click()


# # Question:3

# In[ ]:


driver=webdriver.Chrome()


# In[34]:


driver.get("https://www.google.com")


# In[35]:


input_button=driver.find_elements(By.CLASS_NAME,"gLFyf")


# In[ ]:





# In[36]:


search=driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')


# # Fruits Image

# In[37]:


product_name=input("enter product name ")
input_button[0].send_keys(product_name)
search[0].click                                           


# In[105]:


image=[]
fruit_img=driver.find_elements(By.XPATH,'//img')
for i in fruit_img:
    image.append(i.get_attribute('src'))
x=image[0:10]
df3=pd.DataFrame(x)
df.to_csv('fruit_img.csv')


# # car image

# In[ ]:





# In[6]:


driver.get("https://www.google.com")


# In[7]:


input_button=driver.find_elements(By.CLASS_NAME,"gLFyf")


# In[8]:


search=driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')


# In[9]:


product_name=input("enter product name ")
input_button[0].send_keys(product_name)
search[0].click                                           


# In[31]:


v=[]
id=driver.find_elements(By.XPATH,('//img[@class="rg_i Q4LuWd"]'))
for i in id:
    src=i.get_attribute('src')
    #print(src)
    v.append(src)
image=v[0:10]    
df4=pd.DataFrame(image)
df4.to_csv("carimg.csv")


# # cakes_Image

# In[ ]:


driver=webdriver.Chrome()


# In[117]:


driver.get("https://www.google.com")


# In[118]:


input_button=driver.find_elements(By.CLASS_NAME,"gLFyf")


# In[119]:


search=driver.find_elements(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')


# In[120]:


product_name=input("enter product name ")
input_button[0].send_keys(product_name)
search[0].click                                           


# In[129]:


img=[]
x_path=driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
for y in x_path:
    img.append(y.get_attribute('src'))
cakes_image=img[0:10]    
df5=pd.DataFrame(cakes_image)
df5.to_csv("cakes_image.csv")


# # Question:7

# In[9]:


driver1=webdriver.Chrome()


# In[10]:


driver1.get('http://www.forbes.com/')


# In[11]:


b=driver1.find_elements(By.XPATH,'/html/body/div[1]/footer/div[1]/div[1]/a[2]')
b[0].click()


# In[13]:


B=driver1.find_elements(By.XPATH,'/html/body/div[1]/div/main/div/section/div[2]/div/div/div[1]/div/div[1]/div/div/a/h2')[0].click()


# In[40]:


t=[]
for i in driver1.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]'):
    t.append(i.text.replace("\n"," "))
b=[]
for i in range(0,14):
    
    B=driver1.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]')
    for i in B:
        
        b.append(i.text.replace('\n'," "))
df=pd.DataFrame(b,columns=t)
df.to_csv("Billionaires.csv")


# # Question:9

# In[ ]:





# In[6]:


driver=webdriver.Chrome()


# In[7]:


driver.get('https://www.hostelworld.com/')


# In[8]:


driver.find_elements(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[5]/div/div[1]/a[1]/div/div[1]/span/span')[0].click


# In[10]:


driver.find_elements(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[5]/div/div[1]/a[1]/div/div[1]/img')[0].click()


# In[48]:


n=[]
for i in range(0,4):
    
    j=driver.find_elements(By.XPATH,'//div[@class="property-name"]')

    for i in j:
        n.append(i.text)
Dis=[]
for i in range(0,4):
    
    dis=driver.find_elements(By.XPATH,'//div[@class="property-description"]')
    for i in dis:
        Dis.append(i.text)
lo=[]
for i in range(0,4):
    
    rm=driver.find_elements(By.XPATH,'//div[@class="property-distance"]')
    for i in rm:
        lo.append(i.text.replace('\n',''))        
        
rating=[]
for i in range(0,4):
    
    r=driver.find_elements(By.XPATH,'//div[@class="property-rating"]')
    for i in r:
        rating.append(i.text.replace('\n',''))       
R=[]
for i in range(0,4):
    
    r=driver.find_elements(By.XPATH,'//div[@class="property-accommodations"]')
    for i in r:
        R.append(i.text.replace('\n'," ")) 
        
data=({'PROPERTY_NAME':n,"PROPERTY_DESCRIPTION":Dis,"PROPERTY_LOCATION":lo,"PROPERTY_RATING and REVIEWS":rating,"PROPERTY_RATE":R})
df=pd.DataFrame(data)
df.to_csv("HostelsLondon.csv")


# # Question:8

# In[19]:


driver=webdriver.Chrome()


# In[20]:


driver.get('https://www.youtube.com/watch?v=zFpjB2o0ow0')


# In[21]:


search_input=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')


# In[22]:


search_button=driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button/yt-icon')


# In[10]:


search_input.send_keys('comady vidio')
search_button.click()


# In[78]:


co=[]
for i in range(25):
    
    
    coments=driver.find_elements(By.ID,"content-text")
    for i in coments:
        co.append(i.text)
c=[]
for i in range (25):
    to=driver.find_elements(By.ID,"header-author")
    for i in to:
        c.append(i.text.replace('\n'," "))
        
data=({'COMMENTS':co,"COMMENTS_TIME":c})
df=pd.DataFrame(data)
df.to_csv("youtube_comments.csv")


# In[ ]:


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_con


# In[83]:


driver=webdriver.Chrome()


# In[ ]:


wait=WebDriverWait(driver,10)
driver.get('https://www.gogle.com/maps')
wiait.

