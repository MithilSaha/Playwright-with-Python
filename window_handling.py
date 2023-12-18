from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    #context contains more than one pages
    context = browser.new_context()
    driver = context.new_page()
    driver.goto("https://letcode.in/windows")
    driver.wait_for_selector("//button[@id = 'home']").click()
    open_windows = context.pages
    print(len(open_windows))
    new_driver = open_windows[1]
    '''
    driver will contain the parent page and new_driver will contain child page.
    bring_to_front() method will give give control to the respected page.
    '''
    new_driver.bring_to_front()
    print(new_driver.title())
    print(driver.title())
    new_driver.wait_for_selector("//a[text() = 'Sign up']").click()
    new_driver.close()
    driver.bring_to_front()
    driver.wait_for_selector("//button[@id = 'home']").click()
    print(driver.title())