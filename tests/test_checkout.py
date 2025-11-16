import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

@allure.feature("Checkout")
@allure.story("Full E2E Checkout Flow")
@allure.title("Test Full E2E Checkout for Standard User")
@allure.description("This test verifies the complete checkout flow from login to 'Thank You' message.")
def test_full_checkout_flow(driver, base_url, test_data):
    """
    Tests the entire E2E checkout flow:
    1. Login
    2. Add item to cart
    3. Go to cart & click checkout
    4. Fill out user info
    5. Confirm and finish order
    6. Verify 'Thank You' message
    """
    # --- Page Object Initialization ---
    login_page = LoginPage(driver, base_url)
    inventory_page = InventoryPage(driver, base_url)
    cart_page = CartPage(driver, base_url)
    checkout_one = CheckoutStepOnePage(driver, base_url)
    checkout_two = CheckoutStepTwoPage(driver, base_url)
    checkout_complete = CheckoutCompletePage(driver, base_url)

    # --- Test Data ---
    user = test_data["users"]["standard"]
    item_to_add = "Sauce Labs Backpack"

    # --- 1. Login ---
    with allure.step("1. Login as standard user"):
        login_page.open()
        login_page.login(user["username"], user["password"])

    # --- 2. Add Item ---
    with allure.step("2. Add item to cart"):
        inventory_page.add_item_to_cart(item_to_add)
        inventory_page.go_to_cart()

    # --- 3. Go to Checkout Step 1 ---
    with allure.step("3. Go to Checkout Step 1"):
        assert cart_page.get_item_name() == item_to_add
        cart_page.go_to_checkout()

    # --- 4. Fill User Info ---
    with allure.step("4. Fill User Information"):
        assert checkout_one.get_page_title() == "Checkout: Your Information"
        checkout_one.fill_checkout_info("Test", "User", "12345")

    # --- 5. Confirm Order ---
    with allure.step("5. Confirm Order"):
        assert checkout_two.get_page_title() == "Checkout: Overview"
        assert checkout_two.get_item_name() == item_to_add
        checkout_two.click_finish()

    # --- 6. Verify Completion ---
    with allure.step("6. Verify Completion"):
        assert checkout_complete.get_page_title() == "Checkout: Complete!"
        assert checkout_complete.get_complete_header_text() == "Thank you for your order!"