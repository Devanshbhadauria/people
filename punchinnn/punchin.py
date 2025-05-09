from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = "https://ofbusiness.peoplestrong.com/altLogin.jsf"  # Replace with actual login URL

def punch_in():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(LOGIN_URL)

        # Replace these with actual field IDs or XPaths
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "loginButton").click()

        time.sleep(10)  # Wait for page to load

        # Replace this with actual Punch In button
        punch_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Punch out`')]")
        punch_btn.click()

        print("✅ Punch In successful")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    punch_in()
