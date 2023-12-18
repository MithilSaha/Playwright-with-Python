from playwright.sync_api import sync_playwright


def dialog_handle(dialog):
    if dialog.message == "Hey! Welcome to LetCode":
        print(dialog.message)
        dialog.accept()
    elif dialog.message == "Are you happy with LetCode?":
        print(dialog.message)
        dialog.dismiss()
    elif dialog.message == "Enter your name":
        print(dialog.message)
        dialog.accept("Sample")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    driver = browser.new_page()
    driver.goto("https://letcode.in/alert")
    driver.on('dialog', dialog_handle)
    driver.wait_for_selector("//button[@id = 'accept']").click()
    driver.wait_for_selector("//button[@id = 'confirm']").click()
    driver.wait_for_selector("//button[@id = 'prompt']").click()