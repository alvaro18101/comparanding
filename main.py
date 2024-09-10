from search import WebScrapingFalabella, WebScrapingSodimac
from create_dataset import create_dataset

url_falabella = 'https://www.falabella.com.pe/falabella-pe/search?Ntt='
url_sodimac = 'https://www.sodimac.com.pe/sodimac-pe/buscar?Ntt='
url_linio = 'https://linio.falabella.com.pe/linio-pe/search?Ntt='
url_tottus = 'https://tottus.falabella.com.pe/tottus-pe/search?Ntt=honor+x8'

query = input('Input the search: ')
query = query.strip().replace(' ', '+')

url_falabella += query
url_sodimac += query

falabella_data = WebScrapingFalabella(url_falabella)
sodimac_data = WebScrapingSodimac(url_sodimac)


df_falabella = create_dataset(falabella_data[-1], falabella_data[:-1])
df_sodimac = create_dataset(sodimac_data[-1], sodimac_data[:-1])

df_falabella.to_excel('data_falabella.xlsx', index=False)
df_sodimac.to_excel('data_sodimac.xlsx', index=False)

print(df_falabella)
print(df_sodimac)