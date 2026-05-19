
from src.modules.search_jobs.action.search_page import JobsPage
from src.shared.navigation import Navigation


def main(navigation: Navigation):
    jobs_page = JobsPage(navigation)
    jobs_page.search_jobs()