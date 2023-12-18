from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    driver = browser.new_page()
    driver.goto("https://google.com")
    print(driver.title())
    browser.close()