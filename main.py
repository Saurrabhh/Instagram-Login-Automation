import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = Service("C:\\Program Files (x86)\\chromedriver.exe")

driver = webdriver.Chrome(service=PATH)
driver.get("https://www.instagram.com")
driver.implicitly_wait(5)

try:
    username = driver.find_element(By.NAME, "username")
    # Write your username in place of ****
    username.send_keys("****")

    password = driver.find_element(By.NAME, "password")
    # Write your password in place of ****
    password.send_keys("****")
    password.send_keys(Keys.ENTER)

except:
    print("Username or Password field not found")
else:
    print("Logged In Successfully")

# wait 5 seconds
time.sleep(3)

try:
    not_now = driver.find_element(By.CLASS_NAME, "cmbtv")
    not_now.click()
    time.sleep(3)
    notnow = driver.find_element(By.XPATH, "//*[@class='mt3GC']/button[1]")
    notnow.click()
except:
    print("Not Now not found")


try:
    user_id = driver.find_element(By.CLASS_NAME, "gmFkV")
    user_id_text = user_id.text
    time.sleep(1)

    driver.get(f"https://www.instagram.com/{user_id.text}")
except:
    print("User ID not found")


try:
    name = driver.find_element(By.CLASS_NAME, "Yk1V7")
    name_text = name.text

except:
    print("Name not found")

else:
    print(f"Hello {name_text}!!\nWelcome to your account: {user_id_text}")
    driver.back()


