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

        self.navigation.send_text(selectors["email"], email)
        self.navigation.send_text(selectors["password"], password)
        self.navigation.click(selectors["button_submit"])
        self.navigation.get_elements(selectors["nav_bar"])