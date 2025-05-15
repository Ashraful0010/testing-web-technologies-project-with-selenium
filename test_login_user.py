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

# Step 2: Enter valid login credentials
try:
    driver.find_element(By.NAME, "username").send_keys("opu0010")
    driver.find_element(By.NAME, "password").send_keys("Abcd1234")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    print("✅ Login form submitted.")
except Exception as e:
    print("❌ Error submitting login form:", e)

# Step 3: Wait to see the result (userHome.php should load if successful)
time.sleep(3)
