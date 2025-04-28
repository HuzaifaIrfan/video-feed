from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

SELENIUM_URL = os.getenv('SELENIUM_URL', 'http://localhost:4444/wd/hub')

TARGET_URL = os.getenv('TARGET_URL', 'http://example.com')


def test_insert_pages_through_admin():

    # Connect to remote Chrome browser
    driver = webdriver.Remote(
        command_executor=SELENIUM_URL,
        options=chrome_options
    )

    driver.get(TARGET_URL)
    assert "Example Domain" in driver.title

    print("Test passed!")

    driver.quit()