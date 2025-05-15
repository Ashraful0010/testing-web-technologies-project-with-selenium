from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome driver setup
options = Options()
options.add_experimental_option("detach", True)
service = Service("C:/Users/ai063/selenium_project/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Open user login page
driver.get("http://localhost/final_project/View/login.html")
time.sleep(2)

# Step 2: Login as user
driver.find_element(By.NAME, "username").send_keys("opu0010")
driver.find_element(By.NAME, "password").send_keys("Abcd1234")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)

# Step 3: Navigate to user_edit.php
driver.get("http://localhost/final_project/Model/user_edit.php")
time.sleep(2)

# Step 4: Find and update fields
try:
    driver.find_element(By.NAME, "firstname").clear()
    driver.find_element(By.NAME, "firstname").send_keys("Ashraful")

    driver.find_element(By.NAME, "lastname").clear()
    driver.find_element(By.NAME, "lastname").send_keys("Islam")

    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("opu0010")

    driver.find_element(By.NAME, "phone").clear()
    driver.find_element(By.NAME, "phone").send_keys("01712345678")

    driver.find_element(By.NAME, "dob").clear()
    driver.find_element(By.NAME, "dob").send_keys("2000-01-01")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print("✅ User information form submitted.")
except Exception as e:
    print("❌ Error updating form:", e)

time.sleep(2)
