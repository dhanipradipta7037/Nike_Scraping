from playwright.sync_api import sync_playwright
import pandas as pd
import time

def main():
    with sync_playwright() as p:
        data_url = []
        url = 'https://www.nike.com/id/w/new-mens-shoes-3n82yznik1zy7ok'
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("div#skip-to-products")
        time.sleep(2)

        # scroll down
        for x in range(1, 6):
            page.keyboard.press("End")
            print("scrolling", x)
            time.sleep(2)

        # scrape link
        items = page.locator('//div[@class="product-card__body"]').all()
        time.sleep(2)
        for item in items:
            link_url = item.locator('//a[@class="product-card__link-overlay"]').get_attribute('href')
            data_url.append(link_url)

        for data in data_url:
            print(data)

        browser.close()



if __name__ == '__main__':
    main()