from bs4 import BeautifulSoup
import requests
from pathlib import Path
import os

# def getPrices(raw_price):
#     raw_price = raw_price.split('S/')
#     raw_price = raw_price[1:]
#     return list(map(lambda i: i.strip(), raw_price))

getPrices = lambda raw_price: list(map(lambda i: i.strip(), raw_price.split('S/')[1:]))

# url = 'https://linio.falabella.com.pe/linio-pe/search?Ntt=Messi'
def WebScrapingLinio(query):
    query = str(query)
    query = query.strip().replace(' ', '+')
    url = 'https://linio.falabella.com.pe/linio-pe/search?Ntt='
    url += query
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    pedido_obtenido = requests.get(url, headers=headers)
    html_obtenido = pedido_obtenido.text
    soup = BeautifulSoup(html_obtenido, 'html.parser')

    prices = soup.find_all('div', {'class': 'jsx-2128016101'})
    products_data = soup.find_all('b', {'class': 'jsx-184544934'})
    images = soup.find_all('picture', {'class': 'jsx-1996933093'})

    products_name, products_brand, products_dealer, image_URLs, images_name = [], [], [], [], []

    for i in range(len(prices)):
        prices[i] = getPrices(prices[i].text)

    i = 0
    while True:
        try:
            length = len(prices[i])
            for j in range(length):
                prices.pop(i+1)
            i += 1
        except:
            break

    for i in range(len(products_data)):
        if i%3 == 0:
            products_brand.append(products_data[i].text)
            
        if i%3 == 1:
            products_name.append(products_data[i].text)

        if i%3 == 2:
            products_dealer.append(products_data[i].text)

    for i in range(len(images)):
        image_URLs.append(images[i].img.get('src'))


    BASE_DIR = Path(__file__).resolve().parent.parent
    MEDIA_ROOT = os.path.join(BASE_DIR, 'comparator/static/images/')
    # image_path = '../comparator/static/images/image.jpg'

    j = 0
    
    for i in range(len(image_URLs)):
        with requests.get(image_URLs[i], stream=True) as response:
            if response.status_code == 200:
                image_name = str(j) + '.jpg'
                with open(MEDIA_ROOT + image_name, 'wb') as image:
                    for chunk in response.iter_content(1024):
                        image.write(chunk)
            else:
                image_name = 'no_image.jpg'

                with open(MEDIA_ROOT + image_name) as input_file:
                    with open(str(j)+'.jpg') as output_file:
                        output_file.write(input_file.read())
        images_name.append(image_name)
        j += 1

    return products_name, prices, products_brand, products_dealer, images_name