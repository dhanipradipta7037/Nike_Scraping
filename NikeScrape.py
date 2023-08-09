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
            # title = item.locator('//img[@class="product-card__hero-image css-1fxh5tw"]').get_attribute('alt')
            link_url = item.locator('//a[@class="product-card__link-overlay"]').get_attribute('href')
            # price = item.locator('//div[@data-testid="product-price"]').inner_text().replace(' ','')
            # image = item.locator('//img[@class="product-card__hero-image css-1fxh5tw"]').get_attribute('src')
            data_list = {
                # 'Nama Sepatu': title,
                # 'Harga Sepatu': price,
                # 'Gambar sepatu': image,
                'link sepatu':link_url
            }
            data_item.append(data_list)
            data_url.append(link_url)

        df = pd.DataFrame(data_item)
        df.to_csv('NIKE_v4.csv', index=False)

        for link in data_url:
            print(link)

        print(len(data_url))
        print('Berhasil')



        # scrape detail item
        # data_item = []
        # for link in data_url:
        #     browser = p.chromium.launch()
        #     page = browser.new_page()
        #     page.goto(link)
        #     page.wait_for_selector("div#__next")
        #     time.sleep(5)
        #     try:
        #         nama = page.locator('//h1[@data-test="product-title]').inner_text()
        #         harga = page.locator('//div[@data-test="product-price"]').inner_text()
        #         size = page.locator('//label[@class="css-xf3ahq"]').inner_text()
        #     except:
        #         nama = 'none'
        #         harga = 'none'
        #         size = 'none'
        #
        #     list_item = {
        #         'Nama':nama,
        #         'Harga':harga,
        #         'Size':size,
        #     }
        #     data_item.append(list_item)
        #
        # #save file
        # df = pd.DataFrame(data_item)
        # print(df)

        browser.close()


if __name__ == '__main__':
    main()