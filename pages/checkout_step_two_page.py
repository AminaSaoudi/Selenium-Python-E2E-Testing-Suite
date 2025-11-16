from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutStepTwoPage(BasePage):
    """
    Page Object for the second step of checkout (overview).
    """
    PATH = "/checkout-step-two.html"

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    FINISH_BUTTON = (By.ID, "finish")

    def get_page_title(self):
        """Returns the text of the page title."""
        return self.get_text(self.PAGE_TITLE)

    def get_item_name(self):
        """Returns the text of the first item in the overview."""
        return self.get_text(self.ITEM_NAME)

    def click_finish(self):
        """Clicks the 'Finish' button to complete the order."""
        self.click(self.FINISH_BUTTON)