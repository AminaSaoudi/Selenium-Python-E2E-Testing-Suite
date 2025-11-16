from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutCompletePage(BasePage):
    """
    Page Object for the final 'Thank You' page.
    """
    PATH = "/checkout-complete.html"

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def get_page_title(self):
        """Returns the text of the page title."""
        return self.get_text(self.PAGE_TITLE)

    def get_complete_header_text(self):
        """Returns the 'Thank You' message text."""
        return self.get_text(self.COMPLETE_HEADER)