
from src.shared.navigation import Navigation
from src.modules.search_jobs.common.selectors import selectors
from src.shared.contants.urls import JOBS_URL

class JobsPage:
    def __init__(self, navigation: Navigation):
        self.navigation = navigation
    
    def search_jobs(self):
        self.navigation.goto_url(JOBS_URL)
        self.navigation.send_text(selectors["input_search"], "RPA Junior")
        