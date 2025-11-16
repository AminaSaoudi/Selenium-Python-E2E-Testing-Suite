from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutStepOnePage(BasePage):
    """
    Page Object for the first step of checkout (user info).
    """
    PATH = "/checkout-step-one.html"

    # Locators
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    PAGE_TITLE = (By.CLASS_NAME, "title")

    def get_page_title(self):
        """Returns the text of the page title."""
        return self.get_text(self.PAGE_TITLE)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        """Fills in the user's information and clicks continue."""
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)