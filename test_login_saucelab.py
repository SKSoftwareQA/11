import pytest
from playwright.sync_api import sync_playwright
#generating the HTML report-"pytest --html=mytestreport.html"

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


def test_login1(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('standard_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    page.wait_for_timeout(3000)
    page.screenshot(path="./Screenshots/1.png")


def test_login2(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('locked_out_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    page.wait_for_timeout(3000)
    page.screenshot(path="./Screenshots/2.png")  

def test_login3(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('problem_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    page.wait_for_timeout(3000)
    page.screenshot(path="./Screenshots/3.png") 

def test_login4(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('performance_glitch_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    page.wait_for_timeout(3000)
    page.screenshot(path="./Screenshots/4.png") 

def test_login5(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('error_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    page.wait_for_timeout(3000)
    page.screenshot(path="./Screenshots/5.png") 

def test_login6(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('visual_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    page.wait_for_timeout(3000)
    page.screenshot(path="./Screenshots/6.png") 


def test_login7(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('visual_user123')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    pagetesturl = page.url
    if pagetesturl == "https://www.saucedemo.com/":
       print("*****************************Invalid usre name*****************************")
       assert True
    else:
       print("***************************failed*******************")
       assert False

def test_login8(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('visual_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce321')
    page.wait_for_selector("//input[@id='login-button']").click()
    pagetesturl = page.url
    if pagetesturl == "https://www.saucedemo.com/":
       print("*****************************Invalid password*****************************")
       assert True
    else:
       print("***************************failed*******************")
       assert False

def test_add_product_to_cart(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('visual_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    page.wait_for_timeout(3000)
    page.wait_for_selector("//button[@id='add-to-cart-sauce-labs-backpack']").click()
    page.wait_for_selector("//a[@class='shopping_cart_link']").click()
    page.screenshot(path="./Screenshots/addproduct_cart.png") 


def test_remove_product_from_cart(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('visual_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    page.wait_for_timeout(3000)
    page.wait_for_selector("//button[@id='add-to-cart-sauce-labs-backpack']").click()
    page.wait_for_selector("//a[@class='shopping_cart_link']").click()
    page.wait_for_selector("//button[@id='remove-sauce-labs-backpack']").click()
    page.screenshot(path="./Screenshots/removeproductfrom_cart.png")

def test_sort_by_priceLOWHI(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('visual_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    select_dropdown = page.query_selector("//select[@class='product_sort_container']")
    select_dropdown.select_option("lohi")
    page.screenshot(path="./Screenshots/sort_by_priceLOHI.png")

def test_sort_by_priceHILOW(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('visual_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    select_dropdown = page.query_selector("//select[@class='product_sort_container']")
    select_dropdown.select_option("hilo")
    page.screenshot(path="./Screenshots/sort_by_priceHILO.png")


def test_sort_by_A2Z(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('visual_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    select_dropdown = page.query_selector("//select[@class='product_sort_container']")
    select_dropdown.select_option("az")
    page.screenshot(path="./Screenshots/sort_by_A2Z.png")

    
def test_sort_by_Z2A(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('visual_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    select_dropdown = page.query_selector("//select[@class='product_sort_container']")
    select_dropdown.select_option("za")
    page.screenshot(path="./Screenshots/sort_by_Z2A.png")  

def test_logout(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('visual_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    page.wait_for_selector("//button[@id='react-burger-menu-btn']").click()
    page.wait_for_selector("//a[@id='logout_sidebar_link']").click()
    page.screenshot(path="./Screenshots/logout.png")

def test_noID_noPwd(page):
    print("Hello WOrld is typing")
    page.goto("https://www.saucedemo.com/")
    page.get_by_text("Login").click()
    #page.get_by_role('button').click()
    # print("page url is", page.url)
    # page.screenshot(path="./Screenshots/noIDnoPWD.png")
    #page.get_by_placeholder("Username").fill("SeetaRam")
    page.screenshot(path="./Screenshots/noIDnoPWD.png")



    if page.url == "https://www.saucedemo.com/inventory.html":
        page.wait_for_timeout(2000)
        print("Invalid Username and Invalid Password Login passed")
        assert False
    else:
        print("Invalid Username and Invalid Password Login failed successfully")
        page.wait_for_timeout(2000)
        assert True

