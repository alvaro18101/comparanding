from .WebScraping import WebScraping
from .create_dataset import create_dataset

# query = input('Input the search: ')
def DoWebScraping(query):
    query = str(query)
    query = query.strip().replace(' ', '+')

    url_falabella = 'https://www.falabella.com.pe/falabella-pe/search?Ntt='
    url_sodimac = 'https://www.sodimac.com.pe/sodimac-pe/buscar?Ntt='
    url_linio = 'https://linio.falabella.com.pe/linio-pe/search?Ntt='
    url_tottus = 'https://tottus.falabella.com.pe/tottus-pe/search?Ntt='

    url_falabella += query
    url_sodimac += query
    url_linio += query
    url_tottus += query

    falabella_data = WebScraping(url_falabella)
    sodimac_data = WebScraping(url_sodimac)
    linio_data = WebScraping(url_linio)
    tottus_data = WebScraping(url_tottus)

    title_falabella = falabella_data[-2]
    title_sodimac = sodimac_data[-2]
    title_linio = linio_data[-2]
    title_tottus = tottus_data[-2]

    # df_falabella.to_excel('data_falabella.xlsx', index=False)
    # df_sodimac.to_excel('data_sodimac.xlsx', index=False)
    # df_falabella.to_excel('data_linio.xlsx', index=False)
    # df_sodimac.to_excel('data_tottus.xlsx', index=False)

    return None

print(DoWebScraping('celulares'))