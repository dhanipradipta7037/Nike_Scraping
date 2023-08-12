import requests
import chompjs
import pandas as pd
import time
from bs4 import BeautifulSoup
import json

df = pd.read_csv('NIKE_v5.csv')
print(df['link sepatu'].head(5))
data_images = []
all_data = []
for link in df['link sepatu']:
    time.sleep(5)
    respon = requests.get(link)
    html = BeautifulSoup(respon.text, 'html.parser')
    try:
        products = html.find('h1',{'data-test':'product-title'}).text.strip()
    except:
        products = 'none'

    try:
        price = html.find('div', {'data-test':'product-price'}).text.strip()
    except:
        price = 'none'

    try:
        rating = html.find('p', {'class':'d-sm-ib pl4-sm'}).text.strip().replace('Stars', '')
    except:
        rating = 'none'
    try:
        images = html.find_all('div', {'class':'css-b8rwz8 tooltip-component-container'})
        for image in images:
            list_image = image.find('img').get('src')
            data_images.append(list_image)
    except:
        data_images = 'none'

    try:
        reviews = html.find('h3', {'class':'headline-4 css-xd87ek'}).text.strip().replace('Reviews','').replace('(','').replace(')','')
    except:
        reviews = 'none'

    total_data ={'nama':products,
                 'harga':price,
                 'rating':rating,
                 'reviews':reviews,
                 'gambar':data_images,
                 }
    all_data.append(total_data)

df2 = pd.DataFrame(all_data)
print(df2)
df2.to_csv('data_6.csv', index=False)



# for data in df['link sepatu'].head(5):
#     time.sleep(5)
#     respon = requests.get(data)
#     html = BeautifulSoup(respon.text, 'html.parser')
#     products = html.find('script',{'type':'application/ld+json'})
#     for product in products:
#         list_item = chompjs.parse_js_object(product)
#         name = list_item['name']
#         try:
#             price = list_item['offers']['lowPrice']
#         except:
#             price = 'none'
#         try:
#             rating = list_item['aggregateRating']['ratingValue']
#         except:
#             rating = 'none'
#         list_data = {'Nama':name,
#                      'Harga':price,
#                      'Rating':rating}
#         data_items.append(list_data)
#
# for item in data_items:
#     print(item)



