from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get('https://www.ajio.com/men-backpacks/c/830201001')
time.sleep(2)

oldHeight = driver.execute_script('return document.body.scrollHeight')


counter = 1
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(7)

    newHeight = driver.execute_script('return document.body.scrollHeight')
    print(counter)
    counter+=1
    print(oldHeight)
    print(newHeight)

    if newHeight == oldHeight:
        break
    
    oldHeight = newHeight

html = driver.page_source

with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)