import chompjs
import pandas as pd
import requests
from selectolax.parser import HTMLParser
import time


df = pd.read_csv('NIKE_v5.csv')
data_scrape = []
print(df['link sepatu'].head())
for url in df['link sepatu'].head():
    time.sleep(5)
    r = requests.get(url)
    data = HTMLParser(r.text)
    products = data.css('script[type="application/ld+json"]')
    for product in products:
        try:
            list_item = chompjs.parse_js_object(product.text())
            list_data = {
                'Nama':list_item['name'],
                'Harga':list_item['offers']['lowPrice'],
                'Rating':list_item['aggregateRating']['ratingValue'],
                'Image':list_item['image']
            }
            data_scrape.append(list_data)
        except:
            pass
    time.sleep(5)

df_data = pd.DataFrame(data_scrape)
print(df_data)
df_data.to_csv('data_scraper_4.csv', index=False)

# links = 'https://www.nike.com/id/t/air-max-1-shoes-ZCSX34/FD9082-100'
# r = requests.get(links)
# data = HTMLParser(r.text)
# products = data.css('script[type="application/ld+json"]')
# for product in products:
#     list_item = chompjs.parse_js_object(product.text())
#     print(list_item['aggregateRating']['ratingValue'])