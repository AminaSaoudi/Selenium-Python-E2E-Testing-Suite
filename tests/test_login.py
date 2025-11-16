from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(driver, base_url, test_data):
    """
    Tests the standard_user can successfully log in.
    """
    # Get user data
    user = test_data["users"]["standard"]

    #Initialize page objects
    login_page = LoginPage(driver, base_url)
    inventory_page = InventoryPage(driver, base_url) 

    # --- Test Steps ---
    login_page.open()
    login_page.login(user["username"], user["password"])

    # --- Assertion ---
    assert inventory_page.get_page_title() == "Products"
    assert inventory_page.is_shopping_cart_displayed()

def test_locked_out_user_login(driver, base_url, test_data):
    """
    Tests that a locked_out_user sees the correct error message.
    """
    # Get user and error data
    user = test_data["users"]["locked_out"]
    expected_error = test_data["error_messages"]["locked_out"]

    # Initialize Page Object
    login_page = LoginPage(driver, base_url)

    # --- Test Steps ---
    login_page.open()
    login_page.login(user["username"], user["password"])

    # --- Assertion ---
    expected_error = "Epic sadface: Sorry, this user has been locked out."
    assert login_page.get_error_message() == expected_error