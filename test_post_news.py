from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome setup
options = Options()
options.add_experimental_option("detach", True)
service = Service("C:/Users/ai063/selenium_project/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Open admin login page
driver.get("http://localhost/final_project/View/adminlogin.html")
time.sleep(2)

# Step 2: Login as admin
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)

# Step 3: Navigate to post_news.php
driver.get("http://localhost/final_project/Model/post_news.php")
time.sleep(2)

# Step 4: Check if form fields exist
try:
    title_input = driver.find_element(By.NAME, "news_title")
    content_textarea = driver.find_element(By.NAME, "news_content")
    submit_button = driver.find_element(By.ID, "submit")
    print("✅ News form fields are present.")
except:
    print("❌ One or more news form fields are missing.")

# Step 5: Fill in the form and submit
title_input.send_keys("Selenium Test News")
content_textarea.send_keys("This news was added through automated testing using Selenium.")
submit_button.click()
print("✅ Submitted news form.")

# Optional: Wait and check for a success or error message
time.sleep(2)
try:
    message_div = driver.find_element(By.CLASS_NAME, "message")
    print("✅ Message displayed:", message_div.text)
except:
    print("❌ No success/error message found after submission.")
