from pathlib import Path
from threading import Thread

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.remote.webdriver import WebDriver

chrome_dr = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    options=ChromeOptions()
)
firefox_dr = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    options=FirefoxOptions()
)
edge_dr = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    options=EdgeOptions()
)


def test(dr: WebDriver):
    dr.get('https://www.google.com')
    time.sleep(5)
    fn = Path(f"/app/screenshot/{dr.name}")
    fn.mkdir(parents=True, exist_ok=True)
    dr.save_screenshot(fn / "1.png")
    dr.quit()


def main():
    threads = []
    for dr in [chrome_dr, firefox_dr, edge_dr]:
        t = Thread(target=test, args=(dr,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
