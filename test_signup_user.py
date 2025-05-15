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

# Step 1: Open the signup page
driver.get("http://localhost/final_project/View/signup.html")
time.sleep(2)

# Step 2: Fill the signup form
try:
    driver.find_element(By.NAME, "firstname").send_keys("Ashraful")
    driver.find_element(By.NAME, "lastname").send_keys("Islam")
    driver.find_element(By.NAME, "username").send_keys("opu_test")
    driver.find_element(By.NAME, "phone").send_keys("01700000000")
    driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
    driver.find_element(By.NAME, "email").send_keys("opu_test@email.com")
    driver.find_element(By.NAME, "password").send_keys("Test@1234")
    driver.find_element(By.NAME, "confirm_password").send_keys("Test@1234")
    
    # Step 3: Click the submit button
    driver.find_element(By.CLASS_NAME, "submit-btn").click()
    print("✅ Signup form submitted.")
except Exception as e:
    print("❌ Error in signup form submission:", e)

# Step 4: Wait to observe the result
time.sleep(3)
