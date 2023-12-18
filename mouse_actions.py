from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    driver = context.new_page()
    driver.goto("https://letcode.in/test")
    #Mouser Hovering
    driver.wait_for_selector("//a[text() = 'Courses']").hover()
    driver.wait_for_selector("//a[text() = ' Playwright ']").hover()
    #Shift + Mouse Right Click
    driver.wait_for_selector("//a[text() = ' Playwright ']").click(button="right")
    #Shift + Mouse Left Click
    driver.wait_for_selector("//a[text() = ' Playwright ']").click(modifiers=["Shift"])