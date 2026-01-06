import pytest
from playwright.sync_api import Page
@pytest.mark.only_browser("chromium")

def test_no_broken_images(page: Page):
    page.goto("https://blsky.tech/", timeout=60000, wait_until="domcontentloaded")
    page.wait_for_timeout(3000)
    images = page.locator("img").all()
    broken_images = []

    for image in images:
        if image.is_visible() == False:
            continue
        width = image.evaluate("(element) => element.naturalWidth") ## Get natural width of image to check if it's loaded
        if width == 0:
            src = image.get_attribute("src")
            broken_images.append(src)
            print(f"Broken image found: {src}") # Log broken image src

    assert len(broken_images) == 0, f"Broken images found: {broken_images}" # Assert no broken images found, if found = test fail 

def test_css_js_loaded(page: Page):
    failed_resources = []
    def check_response(response):
        url = response.url
        
        if url.endswith(".css") or url.endswith(".js"): #check CSS and JS files
            status = response.status
            if status >= 400:
                failed_resources.append(url)
                print(f"Failed to load: {url} - Status: {status}")
    
    page.on("response", check_response)
    page.goto("https://blsky.tech/", wait_until="domcontentloaded")
    page.wait_for_timeout(3000)
    assert len(failed_resources) == 0, f"Found {len(failed_resources)} failed assets"