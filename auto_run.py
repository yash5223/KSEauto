from playwright.sync_api import sync_playwright

def fetch_page():
    url = "https://kse.infinityfreeapp.com/autoupdatetime.php?i=1"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle")  # Wait for JavaScript execution
        print("Page loaded successfully")
        browser.close()

if __name__ == "__main__":
    fetch_page()
