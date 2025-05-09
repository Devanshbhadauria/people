from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import os
import time

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = "https://ofbusiness.peoplestrong.com/altLogin.jsf"

def punch_in():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = None

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        print("🌐 Opening login page...")
        driver.get(LOGIN_URL)

        print("⌛ Waiting for username field...")
        username_field = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys(USERNAME)

        print("⌛ Waiting for password field...")
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(PASSWORD)

        print("🔐 Clicking login button...")
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "loginButton"))
        )
        login_button.click()

        print("⌛ Waiting for Punch In button...")
        punch_btn = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Punch In')]"))
        )
        punch_btn.click()

        print("✅ Punch In successful")

    except Exception as e:
        print(f"❌ Error: {e}")
        if driver:
            with open("punchin-failure.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            driver.save_screenshot("punchin-failure.png")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    punch_in()
