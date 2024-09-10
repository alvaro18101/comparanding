from search import WebScraping
from create_dataset import create_dataset

url_falabella = 'https://www.falabella.com.pe/falabella-pe/search?Ntt='
url_sodimac = 'https://www.sodimac.com.pe/sodimac-pe/buscar?Ntt='
url_linio = 'https://linio.falabella.com.pe/linio-pe/search?Ntt='
url_tottus = 'https://tottus.falabella.com.pe/tottus-pe/search?Ntt=honor+x8'

query = input('Input the search: ')
query = query.strip().replace(' ', '+')

url = url_falabella + query

product_name, product_prices, product_type, product_business, columns = WebScraping(url)

df = create_dataset(columns, (product_name, product_prices, product_type, product_business))
df.to_excel('data.xlsx', index=False)
print(df)