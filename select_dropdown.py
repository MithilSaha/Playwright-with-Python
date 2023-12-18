from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    driver = browser.new_page()
    driver.goto("https://www.saucedemo.com/")

    driver.wait_for_selector("#user-name").type("standard_user")
    driver.wait_for_selector("input[name='password']").type("secret_sauce")
    driver.wait_for_selector(".submit-button").click()

    driver.select_option("//select[@class = 'product_sort_container']", label = "Price (low to high)")