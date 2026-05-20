from src.shared.navigation import Navigation
from src.modules.login_user.main import main as login_user
from src.modules.search_jobs.main import main as search_jobs
from src.shared.contants.urls import BASE_URL
from dotenv import load_dotenv

load_dotenv()

def main():
    navigation = Navigation(BASE_URL)
    if login_user(navigation):
        jobs = search_jobs(navigation)

    navigation.browser.close()
    return jobs

