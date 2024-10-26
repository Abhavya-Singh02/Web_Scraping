from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time 

# create a service object
service = Service(ChromeDriverManager().install())

# Create a WebDriver instance
driver = webdriver.Chrome(service=service)
driver.get('http://google.com')
time.sleep(2)

user_input = driver.find_element(By.NAME, "q")
user_input.send_keys('campusx')
time.sleep(1)

user_input.send_keys(Keys.ENTER)

link = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
link.click()
time.sleep(1)

enroll = driver.find_element(by=By.XPATH, value='//*[@id="1698390585510d"]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
enroll.click()
time.sleep(1)

