from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

class SimpleEngine:
    def __init__(self, link):
        self.link = link
        self.driver = self.start_browser()

    def start_browser(self):
        opts = Options()
        opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--disable-gpu")

        # Block images, fonts, CSS to load faster
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.managed_default_content_settings.fonts": 2,
        }
        opts.add_experimental_option("prefs", prefs)

        return webdriver.Chrome(options=opts)

    def scrape(self):
        self.driver.get(self.link)

        try:
            WebDriverWait(self.driver, 15).until(
                lambda d: len(d.find_element(By.TAG_NAME, "body").text.strip()) > 50
            )
        except:
            print("Page took too long or has no content.")
            self.driver.quit()
            return

        # Title
        title = self.driver.title
        print(title if title else "No title")
        print()

        # Body text
        body = self.driver.find_elements(By.TAG_NAME, "body")
        for part in body:
            print(part.text)
        print()

        # Links
        print("Links:")
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for tag in links:
            href = tag.get_attribute("href")
            if href:
                print(href)

        self.driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Enter URL")
        sys.exit()

    url = sys.argv[1]
    if not url.startswith("http"):
        url = "https://" + url

    engine = SimpleEngine(url)
    engine.scrape()