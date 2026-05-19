from src.modules.login_user.action.login_user import LoginUserPage
from src.shared.navigation import Navigation
from src.shared.contants.urls import LOGIN_URL, STATE_PATH
from pathlib import Path


def main(navigation: Navigation):    
    caminho = Path(STATE_PATH)
    if caminho.exists():
        navigation.load_auth_context(STATE_PATH)
        return True
    
    navigation.goto_url(LOGIN_URL)
    login_page = LoginUserPage(navigation)
    login_page.fill_login_form()
    
    if login_page.check_is_logged():
        navigation.save_auth()
        return True
    
    return False