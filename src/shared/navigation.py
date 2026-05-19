from playwright.sync_api import sync_playwright

class Navigation():
    
    def __init__(self, url):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto(url)
    
    def goto_url(self,url):
        self.page.goto(url)
    
    def click(self,selector):
        self.page.click(selector)
    
    def send_text(self, selector, text):
        self.page.fill(selector,text)
    
    def get_elements(self,selector):
        return self.page.locator(selector)