from playwright.sync_api import sync_playwright

USERNAMES = [
    "lookonchain",
    "OnchainLens"
]

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for username in USERNAMES:
            url = f"https://x.com/{username}"
            page.goto(url, timeout=60000)
            page.wait_for_timeout(5000)

            tweets = page.locator("article div[data-testid='tweetText']")
            count = tweets.count()

            print(f"\n--- {username} ---")
            for i in range(min(5, count)):
                print("-", tweets.nth(i).inner_text())

        browser.close()

if __name__ == "__main__":
    run()
