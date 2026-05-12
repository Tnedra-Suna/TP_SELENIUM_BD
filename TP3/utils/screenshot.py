import os
from datetime import datetime
from utils.logger import get_logger

logger = get_logger("screenshot")

def take_screenshot(driver, name: str) -> str:
    """Capture d'écran"""
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(filename)
    logger.info(f"Screenshot sauvegardé : {filename}")
    return filename