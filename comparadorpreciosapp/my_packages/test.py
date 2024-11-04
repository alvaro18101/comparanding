from bs4 import BeautifulSoup
import requests

url = 'https://listado.mercadolibre.com.pe/celular#D[A:celular]'
url = 'https://listado.mercadolibre.com.pe/celulares-telefonos/celulares-smartphones/celular_NoIndex_True'
url = 'https://listado.mercadolibre.com.pe/celular'


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://www.example.com",
    "Accept-Language": "en-US,en;q=0.9"
}

pedido_obtenido = requests.get(url, headers=headers)
html_obtenido = pedido_obtenido.text
soup = BeautifulSoup(html_obtenido, 'html.parser')

products_name = soup.find_all('h2', {'class': 'poly-box poly-component__title'})
for i in range(len(products_name)):
    products_name[i] = products_name[i].text

products_brand = soup.find_all('span', {'class': 'poly-component__seller'})

divs = soup.find_all('div', {'class': 'poly-card poly-card--list'})

# for i in divs:
    # print(divs.index(i), i.find('h2', {'class': 'poly-box poly-component__title'}).text)
div10 = divs[8]

name = div10.find('h2', {'class': 'poly-box poly-component__title'}).text
prices = div10.find('div', {'class': 'poly-component__price'})
link = div10.find('a').get('href')
image_link = div10.img.get('src')
normal_price = prices.find('s').text
offer_price = div10.find('span', {'class': 'andes-money-amount'}).text
off = div10.find('span', {'class': 'andes-money-amount__discount'}).text
seller = div10.find('span', {'class': 'poly-component__seller'}).text

print(f'Nombre: {name}')
print(f'Precio normal: {normal_price}')
print(f'Precio de oferta: {offer_price}')
print(f'Oferta: {off}')
print(f'Vendedor: {seller}')
print(f'Enlace: {link}')
print(f'Enlace a imagen: {image_link}')
print()

# d2 = div10.find('div', {'class': 'poly-card__content'})