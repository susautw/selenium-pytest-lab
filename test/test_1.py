import time
from pathlib import Path


def test_open_google(driver):
    driver.get('https://www.google.com')
    time.sleep(5)
    fn = Path(f"/app/screenshot/{driver.name}")
    fn.mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(fn / "1.png")


def test_open_python(driver):
    driver.get('https://www.python.org/')
    time.sleep(5)
    fn = Path(f"/app/screenshot/{driver.name}")
    fn.mkdir(parents=True, exist_ok=True)
    driver.save_screenshot(fn / "2.png")
