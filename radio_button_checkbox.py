from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1500)
    driver = browser.new_page()
    driver.goto("https://letcode.in/forms")
    element  = driver.query_selector("//input[@id = 'male']")
    element.scroll_into_view_if_needed()
    element.click()
    driver.query_selector("//input[@id = 'female']").click()
    driver.query_selector("//input[@type = 'checkbox']").check()