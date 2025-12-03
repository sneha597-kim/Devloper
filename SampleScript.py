import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Test Execution Started")

# Path to Edge WebDriver
driver_path = "C:\\Program Files\\WebDriver\\msedgedriver.exe"
service = Service(driver_path)

# Create Edge WebDriver instance
driver = webdriver.Edge(service=service)

try:
    driver.maximize_window()
    driver.get("http://localhost:8082/index.html")
    print("Navigating to the form...")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "firstName")))

    driver.find_element(By.ID, "firstName").send_keys("TestUser")
    driver.find_element(By.ID, "lastName").send_keys("Example")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "phNo").send_keys("1234567890")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Thank You For Registering :)")
    )

    if "Thank You For Registering :)" in driver.page_source:
        print("✅ Test Passed!")
    else:
        print("❌ Test Failed!")
finally:
    driver.quit()
    print("Test Execution Completed Successfully!")

import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Pizza Order Test Started")

# Path to Edge WebDriver
driver_path = "C:\\Program Files\\WebDriver\\msedgedriver.exe"
service = Service(driver_path)

driver = webdriver.Edge(service=service)

try:
    driver.maximize_window()
    driver.get("http://localhost:8082/pizza.html")
    print("Opening Pizza Order Form...")

    wait = WebDriverWait(driver, 10)

    # Wait for the customer name input to load
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))

    # Fill customer name (first text input)
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Sneha Customer")

    # Select pizza size: Medium (2nd radio)
    driver.find_element(By.XPATH, "//input[@type='radio' and @value='Medium']").click()

    # Select toppings:
    driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='Cheese']").click()
    driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='Paneer']").click()

    # Fill address (textarea)
    driver.find_element(By.XPATH, "//textarea").send_keys("D.No: 123, Hyderabad, Telangana")

    # Click Order Now
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    print("✅ Pizza Order Form Submitted Successfully!")

finally:
    time.sleep(5)  # keep browser open for 5 seconds
    driver.quit()
    print("Test Finished Successfully!")
