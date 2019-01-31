from packages.tel_scraper import TelSearch, LocalCH, utils

import re

query_dict={
    'was': 'Popp',
    'wo': '',
    'category': ''
}

df_all = LocalCH.page_aggregator(query_dict, max_pages=1)

url_tels = TelSearch.generate_search_url(was=query_dict['was'], wo=query_dict['wo'], category=query_dict['category'])
url_local = LocalCH.generate_search_url(was=query_dict['was'], wo=query_dict['wo'], category=query_dict['category'])
page = utils.get_one_page(url_local)
result_info = page.body.small.text.replace('\n','')
entry_count = re.search(r"\d+", result_info)[0]
# df_tels = TelSearch.df_from_page(tel_search_url=url_tels)
# df_local = LocalCH.df_from_page(local_ch_search_url=url_local)

# df_all = TelSearch.page_aggregator(query_dict, max_pages=21)
# print(df_all)

