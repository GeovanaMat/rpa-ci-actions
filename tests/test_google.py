from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto("https://google.com")
        
        assert "Google" in page.title()
        print("Page Title",page.title())
        browser.close()
