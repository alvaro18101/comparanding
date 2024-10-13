from bs4 import BeautifulSoup
import requests

def WebScraping(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    pedido_obtenido = requests.get(url, headers=headers)
    html_obtenido = pedido_obtenido.text
    soup = BeautifulSoup(html_obtenido, 'html.parser')

    title = soup.find('title').text

    product_scraping = soup.find_all('b', {'class': 'jsx-33793501'})
    product_offer_prices = soup.find_all('li', {'class': 'jsx-2128016101 prices-1'})
    product_normal_prices = soup.find_all('div', {'class': 'jsx-2128016101 prices prices-2_GRID'})

    product_type, product_name, product_business = [], [], []
    for i in range(len(product_scraping)):
        if i%3 == 0:
            product_type.append(product_scraping[i].text)
        if i%3 == 1:
            product_name.append(product_scraping[i].text)
        if i%3 == 2:
            product_business.append(product_scraping[i].text)

    # for i in range(len(product_normal_prices)):
    #     product_normal_prices[i] = product_normal_prices[i].text
    #     product_offer_prices[i] = product_offer_prices[i].text

    # for i in range(len(product_name)):
    #     print(i, product_name[i])
    # print()

    # for i in range(len(product_normal_prices)):
    #     print(i, product_normal_prices[i])
    # print()

    # for i in range(len(product_offer_prices)):
    #     print(i, product_offer_prices[i])
    # print()

    # for i in range(len(product_type)):
    #     print(i, product_type[i])
    # print()

    # for i in range(len(product_business)):
    #     print(i, product_business[i])
    # print()

    columns = ['Nombre', 'Precio normal', 'Precio de oferta', 'Tipo', 'Negocio']
    columns = ['Nombre']
    # return product_name, product_normal_prices, product_offer_prices, product_type, product_business, columns
    return product_name, title, columns

# img = soup.find('img')