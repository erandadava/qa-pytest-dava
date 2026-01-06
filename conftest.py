import pytest
from playwright.sync_api import Page

@pytest.fixture
def page(page: Page):
    # Set default timeout untuk semua test
    page.set_default_timeout(100000)
    page.set_default_navigation_timeout(100000)
    return page