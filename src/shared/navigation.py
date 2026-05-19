from playwright.sync_api import sync_playwright
from src.shared.contants.urls import STATE_PATH

class Navigation():
    
    def __init__(self, url):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch()
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto(url)
    
    def goto_url(self,url):
        self.page.goto(url)
    
    def click(self,selector):
        self.page.click(selector)
    
    def send_text(self, selector, text):
        self.page.fill(selector,text)
    
    def get_elements(self,selector):
        return self.page.locator(selector)
    
    def wait_get_element(self, selector, timeout=30000):
        """Aguarda até que o elemento apareça na tela e esteja visível."""
        self.page.wait_for_selector(selector, state="visible", timeout=timeout)
        return self.get_elements(selector)

    def save_auth(self,filename=STATE_PATH):
        self.context.storage_state(path=STATE_PATH)
    
    def load_auth_context(self, filename=STATE_PATH):
        self.page.close()
        self.context.close()
    
        self.context = self.browser.new_context(storage_state=filename)
        self.page = self.context.new_page()