from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):   
    PATH = "/" # path relative to the base_url

    # Locators (using data-test attributes is robust!)
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        """Navigates to the login page."""
        self.driver.get(self.base_url + self.PATH)

    def login(self, username, password):
        """Performs a full login sequence using BasePage methods."""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Returns the text of the login error message."""
        return self.get_text(self.ERROR_MESSAGE)