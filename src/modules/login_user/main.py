from src.modules.login_user.action.login_user import LoginUserPage
from src.shared.navigation import Navigation
from src.shared.contants.urls import LOGIN_URL

def main(navigation: Navigation):
    navigation.goto_url(LOGIN_URL)
    login_page = LoginUserPage(navigation)
    login_page.fill_login_form()