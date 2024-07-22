# login.py
from playwright.sync_api import Page

def login(page: Page, username: str, password: str):
    page.goto('https://example.com/login')
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"]')
    page.wait_for_selector('text=Logged in successfully')


***************************************************
# add_to_cart_test.py
from playwright.sync_api import sync_playwright
from login import login

def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Use the login function
        login(page, 'your_username', 'your_password')

        # Now perform the add to cart steps
        page.goto('https://example.com/products')
        page.click('text=Specific Product')  # Click on the specific product
        page.click('button#add-to-cart')     # Click on 'Add to Cart' button
        
        # Verify item is added to cart
        page.goto('https://example.com/cart')
        assert page.locator('text=Specific Product').is_visible(), "Product not found in cart!"

        browser.close()

if __name__ == '__main__':
    test_add_to_cart()
