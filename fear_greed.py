from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options




def get_fear_greed():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--log-level=3")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://www.cnn.com/markets/fear-and-greed"
    driver.get(url)

    try:
        index_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "market-fng-gauge__dial-number-value"))
        )
        index_value = index_element.text
        print(f"Fear & Greed Index: {index_value}")
    except Exception as e:
        print("Failed to find the Fear & Greed Index value:", e)
    finally:
        driver.quit()
    
    return int(index_value)
