from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setup
service = Service("C:/Users/ai063/selenium_project/drivers/chromedriver.exe")  
options = Options()
options.headless = False  # Show browser for now
driver = webdriver.Chrome(service=service, options=options)

# STEP 1: Open admin login page
driver.get("http://localhost/final_project/View/adminlogin.html")  

# STEP 2: Fill in credentials
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")

# STEP 3: Click the Login button 
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# STEP 4: Wait to load next page
time.sleep(3)

# STEP 5: Check if redirected (can adjust condition)
if "adminHome" in driver.current_url:
    print("Admin login successful!")
else:
    print("Admin login failed!")

driver.quit()
