import os
from src.shared.navigation import Navigation
from src.modules.login_user.common.selectors import selectors
from time import sleep
class LoginUserPage:
    
    def __init__(self, navigation: Navigation):
        self.navigation = navigation
    
    def fill_login_form(self):
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        self.navigation.page.get_by_role("textbox", name="E-mail ou telefone").fill(email)
        self.navigation.page.get_by_role("textbox", name="Senha").fill(password)
        self.navigation.page.get_by_role("button", name="Entrar", exact=True).click()

        #         self.navigation.page.goto("https://www.linkedin.com/jobs/")
        # self.navigation.page.get_by_test_id("typeahead-input").click()
        # self.navigation.page.get_by_test_id("typeahead-input").fill("rpa")
        # self.navigation.page.get_by_test_id("typeahead-input").press("Enter")
    def check_is_logged(self):
        try:
            self.navigation.page.get_by_test_id("primary-nav")
            return True
        except Exception as e:
            return False
            
