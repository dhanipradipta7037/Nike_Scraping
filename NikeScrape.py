from playwright.sync_api import sync_playwright
import pandas as pd
import time

def main():
    with sync_playwright() as p:
        data_item = []
        data_url = []
        url = 'https://www.nike.com/id/w/new-mens-shoes-3n82yznik1zy7ok'
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector("div#skip-to-products")
        time.sleep(10)

        # scroll down
        for x in range(1, 6):
            page.keyboard.press("End")
            print("scrolling", x)
            time.sleep(5)

        # scrape link
        items = page.locator('//div[@class="product-card__body"]').all()
        time.sleep(5)
        for item in items:
            link_url = item.locator('//a[@class="product-card__link-overlay"]').get_attribute('href')
            data_list = {'link sepatu':link_url}
            data_item.append(data_list)

        df = pd.DataFrame(data_item)
        df.to_csv('NIKE_v5.csv', index=False)

        for link in data_item:
            print(link)

        print(len(data_url))
        print('Berhasil')


        browser.close()


if __name__ == '__main__':
    main()