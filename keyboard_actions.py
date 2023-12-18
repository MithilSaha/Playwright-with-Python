from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    driver = browser.new_page()
    driver.goto("https://letcode.in/test")
    driver.wait_for_selector("//a[text() = 'Work-Space']").press("Control+A")
    driver.wait_for_selector("//a[text() = 'Work-Space']").press("PageDown")