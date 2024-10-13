from .search import WebScraping
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

    df_falabella = create_dataset(falabella_data[-1], falabella_data[:-2])
    df_sodimac = create_dataset(sodimac_data[-1], sodimac_data[:-2])
    df_linio = create_dataset(linio_data[-1], linio_data[:-2])
    df_tottus = create_dataset(tottus_data[-1], tottus_data[:-2])

    falabella = (title_falabella, df_falabella.iloc[0:3].values)
    sodimac = (title_sodimac, df_sodimac.iloc[0:3].values)
    linio = (title_linio, df_linio.iloc[0:3].values)
    tottus = (title_tottus, df_tottus.iloc[0:3].values)


    # df_falabella.to_excel('data_falabella.xlsx', index=False)
    # df_sodimac.to_excel('data_sodimac.xlsx', index=False)
    # df_falabella.to_excel('data_linio.xlsx', index=False)
    # df_sodimac.to_excel('data_tottus.xlsx', index=False)

    return falabella, sodimac, linio, tottus

print(DoWebScraping('celulares'))