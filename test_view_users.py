from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Setup
service = Service("C:/Users/ai063/selenium_project/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Step 1: Login as admin
driver.get("http://localhost/final_project/View/adminlogin.html")
time.sleep(1)

driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)

# Step 2: Navigate to view_users.php
driver.get("http://localhost/final_project/Model/view_users.php")
time.sleep(2)

# Step 3: Check users table presence
try:
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    print(f"Users displayed: {len(rows)} row(s)")
except Exception as e:
    print("User table not found:", e)

driver.quit()
