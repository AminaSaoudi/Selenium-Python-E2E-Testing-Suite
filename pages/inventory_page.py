from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    """
    Page Object for the main inventory/products page.
    """
    PATH = "/inventory.html"  # path relative to the base_url
    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART_LINK = (By.ID, "shopping_cart_container")

    def get_page_title(self):
        """Returns the text of the page title."""
        return self.get_text(self.PAGE_TITLE)

    def is_shopping_cart_displayed(self):
        """Checks if the shopping cart icon is visible."""
        try:
            # Use find() which has a built-in wait
            self.find(self.SHOPPING_CART_LINK) 
            return True
        except:
            # find() will raise a TimeoutException if not found
            return False
        
    def add_item_to_cart(self, item_name):
        """
        Finds an item by its name and clicks its 'Add to Cart' button.
        This uses a dynamic 'data-test' attribute for stability.
        """
        # 1. Convert the item name to its 'data-test' format
        # e.g., "Sauce Labs Backpack" -> "add-to-cart-sauce-labs-backpack"
        item_data_test = f"add-to-cart-{item_name.lower().replace(' ', '-')}"

        # 2. Define the new, stable locator
        item_locator = (By.NAME, item_data_test)

        # 3. Click the element
        self.click(item_locator)

    def go_to_cart(self):
        """Clicks the shopping cart icon to navigate to the cart."""
        self.click(self.SHOPPING_CART_LINK)