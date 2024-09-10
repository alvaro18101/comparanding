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

    product_scraping = soup.find_all('b', {'class': 'jsx-3038137090'})
    product_prices = soup.find_all('li', {'class': 'jsx-3604446019 prices-0'})

    product_type, product_name, product_business = [], [], []
    for i in range(len(product_scraping)):
        if i%3 == 0:
            product_type.append(product_scraping[i].text)
        if i%3 == 1:
            product_name.append(product_scraping[i].text)
        if i%3 == 2:
            product_business.append(product_scraping[i].text)

    for i in range(len(product_prices)):
        product_prices[i] = product_prices[i].text
    
    columns = ['Nombre', 'Precio', 'Tipo', 'Negocio']

    return product_name, product_prices, product_type, product_business, columns