import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    """
    This is the correct hook to add custom INI options.
    """
    parser.addini("base_url", help="The base URL for the application under test", default=None)


@pytest.fixture(scope="session")
def base_url(request):
    """
    Fixture to get the base_url from the pytest.ini config file.
    """
    return request.config.getini("base_url")

@pytest.fixture(scope="session")
def test_data():
    """
    Fixture to load test data from the JSON file.
    """
    with open("data/test_data.json") as f:
        data = json.load(f)
    return data


@pytest.fixture(scope="function")
def driver():
    """
    This fixture creates a new REMOTE Chrome WebDriver instance.
    It connects to the 'selenium' service defined in docker-compose.yml.
    """

    # --- Setup Chrome Options ---
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # --- Driver Initialization ---
    # The URL now points to our new service name: 'selenium'
    REMOTE_HUB_URL = "http://selenium:4444/wd/hub"

    # No more try/except. When running in Docker, it MUST
    # connect to this URL, or we want it to fail.
    driver_instance = webdriver.Remote(
        command_executor=REMOTE_HUB_URL,
        options=chrome_options
    )

    yield driver_instance

    # --- Teardown ---
    driver_instance.quit()