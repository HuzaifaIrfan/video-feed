from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

SELENIUM_URL = os.getenv('SELENIUM_URL', 'http://localhost:4444/wd/hub')

APP_HOST = os.getenv('APP_HOST', 'http://example.com/')
print(APP_HOST)

pages_test=[
        {
            "title":"NetworkChuck",
            "url":"https://www.youtube.com/@NetworkChuck/videos",
        },
        {
            "title":"ThePrimeTimeagen",
            "url":"https://www.youtube.com/@ThePrimeTimeagen/videos",
        },
        {
            "title":"TravisMedia",
            "url":"https://www.youtube.com/@TravisMedia/videos",
        },
                        
        {
            "title":"TheCodingSloth",
            "url":"https://www.youtube.com/@TheCodingSloth/videos",
        },
                                
        {
            "title":"TechWorldwithNana",
            "url":"https://www.youtube.com/@TechWorldwithNana/videos",
        },
                                        
        {
            "title":"Fireship",
            "url":"https://www.youtube.com/@Fireship/videos",
        },
                                                
        {
            "title":"IBMTechnology",
            "url":"https://www.youtube.com/@IBMTechnology/videos",
        },
                                                        
        {
            "title":"Computerphile",
            "url":"https://www.youtube.com/@Computerphile/videos",
        },
        {
            "title":"Hussein Nasser",
            "url":"https://www.youtube.com/@hnasr/videos"
        }
    ]

ADMIN_PASSWORD="aa"

def test_insert_pages_through_admin():
    url=APP_HOST

    try:
        # Connect to remote Chrome browser
        driver = webdriver.Remote(
            command_executor=SELENIUM_URL,
            options=chrome_options
        )

        driver.get(url)
        driver.implicitly_wait(10)
        assert "Example Domain" in driver.title
    finally:
        driver.quit()    
        


    print("Test passed!")
    
    

