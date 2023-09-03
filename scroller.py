from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get('https://www.filmweb.pl/search#/films?orderBy=rate.desc&count=12000%2C')
time.sleep(3)
#previous_height = driver.execute_script(' return document.body.scrollHeight')

element = driver.find_element(By.TAG_NAME, 'body')

while True:

    element.send_keys(Keys.PAGE_DOWN)
    #driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 300);')
    time.sleep(1.2)
    #new_height = driver.execute_script('return document.body.scrollHeight')

    

    #if new_height == previous_height:
        #break
    #previous_height = new_height