import pytest
from playwright.sync_api import Page, expect
@pytest.mark.only_browser("chromium")
def test_all_menu_visible(page: Page):
    page.goto("https://blsky.tech/", timeout=60000, wait_until="domcontentloaded")
    expect(page.locator("#nav-link-hero").first).to_be_visible()
    expect(page.locator("#nav-link-testimonies").first).to_be_visible()
    expect(page.locator("#nav-link-values").first).to_be_visible()
    expect(page.locator("#cta-get-in-touch").first).to_be_visible()

def test_home_menu(page: Page):
    page.goto("https://blsky.tech/", timeout=60000, wait_until="domcontentloaded")
    page.click("#nav-link-hero")
    results_heading = page.get_by_role("heading", name="Your Technology Partner")
    expect(results_heading).to_be_visible()

def test_results_menu(page: Page):
    page.goto("https://blsky.tech/", timeout=60000, wait_until="domcontentloaded")
    page.click("#nav-link-testimonies")
    results_heading = page.get_by_role("heading", name="Results")
    expect(results_heading).to_be_visible()

def test_ourprocess_menu(page: Page):
    page.goto("https://blsky.tech/", timeout=60000, wait_until="domcontentloaded")
    page.click("#nav-link-values")
    results_heading = page.get_by_role("heading", name="Our Process")
    expect(results_heading).to_be_visible()