from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_item_to_cart(driver, base_url, test_data):
    """
    Full E2E test:
    1. Login
    2. Add a specific item to the cart
    3. Go to cart
    4. Verify the correct item is in the cart
    """
    login_page = LoginPage(driver, base_url)
    inventory_page = InventoryPage(driver, base_url)
    cart_page = CartPage(driver, base_url)

    user = test_data["users"]["standard"]
    item_to_add = "Sauce Labs Backpack" # The item we'll test

    # --- 1. Login ---
    login_page.open()
    login_page.login(user["username"], user["password"])

    # --- 2. Add Item ---
    # Verify we are on the inventory page
    assert inventory_page.get_page_title() == "Products"

    # Add the item
    inventory_page.add_item_to_cart(item_to_add)

    # --- 3. Go to Cart ---
    inventory_page.go_to_cart()

    # --- 4. Verify ---
    # Verify we are on the cart page
    assert cart_page.get_page_title() == "Your Cart"

    # Verify the correct item is present
    assert cart_page.get_item_name() == item_to_add