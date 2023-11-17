import pytest
from pages.to_do_page import ToDoPage
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def home_page_to_do_list(page: Page):
    to_do_page = ToDoPage(page)
    to_do_page.go_to()
    
    yield to_do_page
