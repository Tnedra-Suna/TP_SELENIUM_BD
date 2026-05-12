import os
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver


def take_screenshot(driver: WebDriver, name: str) -> str:
    os.makedirs("screenshots", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(filename)
    
    return filename