from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    The Base Page class, which all other Page Objects will inherit from.
    """
    def __init__(self, driver, base_url):
        """
        Initialize the Base Page with the WebDriver instance.
        """
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)  # 10-second explicit wait

    def find(self, locator):
        """
        Finds a single element using the specified locator.
        Waits until the element is present.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        """
        Finds all elements using the specified locator.
        Waits until at least one element is present.
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """
        Waits for an element to be clickable, then clicks it.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """
        Finds an element, clears it, and types the given text.
        """
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Finds an element and returns its text content.
        """
        element = self.find(locator)
        return element.text