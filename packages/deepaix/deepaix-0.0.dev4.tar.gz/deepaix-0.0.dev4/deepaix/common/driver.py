import requests
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from deepaix.common.logger import use_logger

logger = use_logger(__name__)


class ChromeDriverService:
    driver: webdriver.Chrome

    def __init__(self, download_path: str = None, enable_logging: bool = False) -> None:
        self.download_path = download_path
        self.enable_logging = enable_logging

    def __enter__(self):
        self._setup_driver()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        logger.info("Quitting the Chrome driver.")

        try:
            self.driver.quit()
        except Exception as e:
            logger.warn(f"Exception in __exit__ while quitting the driver: {e}")

    def _setup_driver(
        self,
    ):
        chrome_options = self._get_chrome_options(
            self.download_path, self.enable_logging
        )

        try:
            driver_path = ChromeDriverManager().install()
            service = Service(executable_path=driver_path)
            self.driver = webdriver.Chrome(
                service=service,
                options=chrome_options,
            )
        except Exception as e:
            logger.warn(
                f"Exception in setup_driver and retry by installing the latest version: {e}"
            )
            latest_version = self._find_latest_chromedriver_version()
            driver_path = ChromeDriverManager(driver_version=latest_version).install()
            service = Service(executable_path=driver_path)
            self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def fetch_network_request_urls(self, url: str) -> list:
        if self.enable_logging == False:
            logger.warn(f"Logging is not enabled to fetch network request URLs.")
            raise Exception(
                "Please enable logging to fetch network request URLs when initializing the driver."
            )

        self.driver.get(url)

        # Fetch the performance logs
        logs = self.driver.get_log("performance")

        # Parse the logs to extract the network request URLs
        urls = []
        for entry in logs:
            log = json.loads(entry["message"])["message"]
            if "Network.requestWillBeSent" in log["method"]:
                if "request" in log["params"]:
                    request = log["params"]["request"]
                    url = request.get("url")
                    if url:
                        urls.append(url)

        return urls

    def wait_driver_until_all_li_inside_ul(self, class_name: str):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        self.driver.implicitly_wait(10)

        elements[0].find_elements(by=By.CSS_SELECTOR, value="li")

    def wait_driver_until_element_by_class_name(self, class_name: str):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))
        self.driver.implicitly_wait(10)

    def wait_driver_until_element_by_name(self, name: str):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.NAME, name)))
        self.driver.implicitly_wait(10)

    def wait_driver_until_element_by_id(self, id: str):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.ID, id)))
        self.driver.implicitly_wait(10)

    @staticmethod
    def _find_latest_chromedriver_version():
        url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        response = requests.get(url)
        version = response.text
        return version

    @staticmethod
    def _get_chrome_options(download_path: str = None, enable_logging: bool = False):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1920,1200")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        if enable_logging:
            logger.info("Enabling performance logging for network requests.")
            perf_logging_prefs = {
                "enableNetwork": True,
                "enablePage": False,
                "enableTimeline": False,
            }
            chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
            chrome_options.set_capability(
                "goog:chromeOptions", {"perfLoggingPrefs": perf_logging_prefs}
            )

        if download_path != None:
            prefs = {"download.default_directory": download_path}
            chrome_options.add_experimental_option("prefs", prefs)

        return chrome_options
