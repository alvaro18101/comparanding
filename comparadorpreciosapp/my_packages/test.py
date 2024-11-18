from bs4 import BeautifulSoup
import requests
import re

# url = 'https://listado.mercadolibre.com.pe/celular#D[A:celular]'
# url = 'https://listado.mercadolibre.com.pe/celulares-telefonos/celulares-smartphones/celular_NoIndex_True'
# url = 'https://listado.mercadolibre.com.pe/celular'

getOFF = lambda string: re.search(r'OFF', string).group()

def WebScrapingMercadoLibre(query):
    query = str(query)
    query = query.strip().replace(' ', '-')
    url = 'https://listado.mercadolibre.com.pe/'
    url += query

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.example.com",
        "Accept-Language": "en-US,en;q=0.9"
    }

    pedido_obtenido = requests.get(url, headers=headers)
    html_obtenido = pedido_obtenido.text
    soup = BeautifulSoup(html_obtenido, 'html.parser')

    divs = soup.find_all('div', {'class': 'poly-card poly-card--list'})

    products_name, products_price, products_brand, products_seller, products_links, image_URLs, images_name = [], [], [], [], [], [], []

    for i in range(len(divs)):
        div = divs[i]
        try:
            name = div.find('h2', {'class': 'poly-box poly-component__title'}).text
        except:
            name = None
        try:
            prices = div.find('div', {'class': 'poly-component__price'})
        except:
            prices = None

        try:
            getOFF(prices.text)
            offer = True
        except:
            offer = False
        if offer:
            try:
                normal_price = prices.find('s', {'class': 'andes-money-amount'}).text
                offer_price = prices.find('span', {'class': 'andes-money-amount'}).text
                off = prices.find('span', {'class': 'andes-money-amount__discount'}).text
            except:
                normal_price = None
                offer_price = None
                off = None
        else:
            try:
                normal_price = prices.find('div', {'class': 'poly-price__current'}).text
            except:
                normal_price = None
                offer_price = None
                off = 0

        try:
            brand = div.find('span', {'class': 'poly-component__brand'}).text
        except:
            brand = 1

        try:
            seller = div.find('span', {'class': 'poly-component__seller'}).text
        except:
            seller = None

        link = div.find('a').get('href')
        image_link = div.img.get('src')

        if name == None or prices == None:
            print('No se pudo')
        else:
            products_name.append(name)
            products_price.append((normal_price, f'{offer_price} -{off}'))
            products_brand.append(brand)
            products_seller.append(seller)
            products_links.append(link)
            image_URLs.append(image_link)
        
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # MEDIA_ROOT = os.path.join(BASE_DIR, 'comparator/static/images/')
    # # image_path = '../comparator/static/images/image.jpg'

    # j = 0
    
    # for i in range(len(image_URLs)):
    #     with requests.get(image_URLs[i], stream=True) as response:
    #         if response.status_code == 200:
    #             image_name = str(j) + '.jpg'
    #             with open(MEDIA_ROOT + image_name, 'wb') as image:
    #                 for chunk in response.iter_content(1024):
    #                     image.write(chunk)
    #         else:
    #             image_name = 'no_image.jpg'

    #             with open(MEDIA_ROOT + image_name) as input_file:
    #                 with open(str(j)+'.jpg') as output_file:
    #                     output_file.write(input_file.read())
    #     images_name.append(image_name)
    #     j += 1

    return products_name, products_price, products_brand, products_seller, products_links, images_name, url

a  = WebScrapingMercadoLibre('celular')
for i in range(len(a[0])):
    print(a[0][i])
    print(a[1][i])
    print()