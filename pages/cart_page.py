from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    """
    Page Object for the Shopping Cart page.
    """
    PATH = "/cart.html"

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_page_title(self):
        """Returns the text of the page title."""
        return self.get_text(self.PAGE_TITLE)

    def get_item_name(self):
        """Returns the text of the first item in the cart."""
        # Note: This is a simple implementation that gets the first item.
        # For a real framework, you'd want to get all items.
        return self.get_text(self.ITEM_NAME)
    
    def go_to_checkout(self):
        """Clicks the 'Checkout' button."""
        self.click(self.CHECKOUT_BUTTON)