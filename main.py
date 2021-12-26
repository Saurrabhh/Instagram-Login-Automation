import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = Service("C:\\Program Files (x86)\\chromedriver.exe")

driver = webdriver.Chrome(service=PATH)
driver.get("https://www.instagram.com")
driver.implicitly_wait(5)
username = driver.find_element(By.NAME, "username")

# Write your username in place of ****
username.send_keys("8401530399")

password = driver.find_element(By.NAME, "password")

# Write your password in place of ****
print(password.get_attribute('outerHTML'))
password.send_keys("$Saurabh5499")
password.send_keys(Keys.ENTER)

print(driver.current_url)
time.sleep(3)

not_now = driver.find_element(By.CLASS_NAME, "cmbtv")
not_now.click()
time.sleep(5)

notnow = driver.find_element(By.XPATH, "//*[@class='mt3GC']/button[1]")
notnow.click()

user_id = driver.find_element(By.CLASS_NAME, "gmFkV")
print(user_id.text)
time.sleep(1)

driver.get(f"https://www.instagram.com/{user_id.text}")

name = driver.find_element(By.CLASS_NAME, "Yk1V7")
print(name.text)
