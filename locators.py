from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    driver = browser.new_page()
    driver.goto("https://www.saucedemo.com/")

    '''CSS Selector'''
    driver.wait_for_selector("#user-name").type("standard_user")
    driver.wait_for_selector("input[name='password']").type("secret_sauce")
    driver.wait_for_selector(".submit-button").click()

    '''XPATH'''
    driver.wait_for_selector("//button[@name = 'add-to-cart-sauce-labs-backpack']").click()
    driver.wait_for_selector("//button[contains(@data-test, 'bike-light')]").click()
    driver.wait_for_selector("//a[@class = 'shopping_cart_link']").click()