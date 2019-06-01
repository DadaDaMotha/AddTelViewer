import pandas as pd

from .model import db_cols
from .. import utils
import re
from urllib.parse import quote_plus as urlquote
import numpy as np
from collections import OrderedDict


entries_per_page = 10

def get_entry_count(page):
    '''

    :param page: parsed html sauce from bs4
    :return:
    '''
    result_info = page.body.small.text.replace('\n', '')
    tmp = re.search(r"\d+", result_info)
    if tmp:
        entry_count = tmp[0]
        return entry_count
    else:
        # Evemtually there is just one on not match
        return 1

def generate_search_url(was='', wo='', category=None, page=None):
    '''

    :param was: Nach was gesucht wird
    :param wo: Wo gesucht wird
    :param category: Private oder Firmen oder nichts (sucht beides)
    :return: url string

    Example urls:

    'https://tel.local.ch/de/q?what=schreiner&where=b%C3%BClach&rid=LyvB#site-navigation-locale-dropdown'
    'https://tel.local.ch/de/q?what=&where=bern&rid=X2Iw'
    'https://tel.local.ch/de/q?what=pfister&where=&rid=pE0h'
    'https://tel.local.ch/de/q/Bern/Steiner.html?page=2&typeref=bus'

    '''

    if was is None:
        was = ''
    if wo is None:
        wo = ''

    mapping = {
        'Private': 'res',
        'Firmen': 'bus'
    }
    url = 'https://tel.local.ch/de/q?'

    url += 'what={}'.format(urlquote(was))
    url += '&where={}'.format(urlquote(wo))

    if category in ['Private', 'Firmen']:
        if not url.endswith('?'):
            url += '&typeref={}'.format(mapping[category])
        else:
            raise AssertionError('Wenistens Ort oder Bezeichnung muss angegeben werden!')

    if page:
        url += '&page={}'.format(page)

    return url


def df_from_page(local_ch_search_url):
    ddict = OrderedDict((key, []) for key in db_cols)
    page = utils.get_one_page(local_ch_search_url)

    containers = page.body.findAll('div', {'class': 'listing-container'})

    for container in containers:
        container.a.find('span', {'class': 'listing-title'})
        container.a.find('div', {'class': 'listing-address'})

        name = container.a.find('span', {'class': 'listing-title'}).text.replace('\n', '')
        try:
            tel = container.find('a', {'class': 'listing-contact-phone'}).attrs['href'][4:]
        except:
            tel = ''

        try:
            website = container.find('a', {'class': 'listing-contact-website'}).attrs['href']
        except:
            website = ''

        addr_tot = container.a.find('div', {'class': 'listing-address'}).text.replace('\n', '')
        # addr_info = re.search(r"^(\w+)\s*(\d+\w*)\s*,\s*(\d+\w*)\s(\w*)", addr_tot)
        # addr_info = re.search(r"\s*(\D*)\s*(\d*\w*)\s*,\s*(\d+\w*)\s(\w*)", addr_tot)
        addr_info = re.search(r"\s*(\D*)\s*(\d*-?/?\d*\w*)\s*,\s*(\d+\w*)\s(\w*)", addr_tot)
        try:
            street = addr_info.group(1).strip()
            street_num = addr_info.group(2)
            plz = addr_info.group(3)
            ort = addr_info.group(4)

        except:
            street = ''
            street_num = np.nan
            plz = np.nan
            ort = ''
        try:
            cat = container.find('div', {'class': 'listing-categories'}).text
        except:
            cat = ''

        ddict['Betriebsart'].append(cat)
        ddict['Bezeichnung'].append(name)
        ddict['Hausnummer'].append(street_num)
        ddict['Ort'].append(ort)
        ddict['PLZ'].append(plz)
        ddict['Strasse'].append(street)
        ddict['Telefon'].append(tel)
        ddict['URL'].append(local_ch_search_url)
        ddict['Website'].append(website)

    df = pd.DataFrame(data=ddict)
    return df

def page_aggregator(query_dict, max_pages=None):
    '''
    :param query_dict: Enthält
        was: Bezeichchung für Beschreibung
        wo: Ortsbezeichnung
        category: Firmen, Private, Alles
    :return: concatenated df from all the pages
    '''
    print(40*'-')
    print('executing page aggregator')
    was = query_dict['was']
    wo = query_dict['wo']
    cat = query_dict['category']

    print('was', was)
    print('wo', wo)
    print('cat', cat)

    if not was and not wo:
        raise AssertionError('Leere Suchanfragget_entry_counte!')

    # create initial url
    url_initial = generate_search_url(was=was, wo=wo, category=cat)
    print('initial url: ', url_initial)
    page = utils.get_one_page(url_initial)
    entry_count = get_entry_count(page)
    print('Total Number of search results: ', entry_count)
    loops = utils.calculate_loops(entries_per_page, entry_count)
    print('--entries per page: {}, total number of loops: {}'.format(entries_per_page, loops))

    df_list = []

    df_initial = df_from_page(url_initial)

    if max_pages:
        if max_pages == 1:
            return df_initial
        elif max_pages < loops:
            loops = max_pages

    df_list.append(df_initial)
    print('fetched {} entries'.format(df_initial.shape[0]))

    for page_num in range(2, loops+1):
        print('loop: ', page_num)
        url = generate_search_url(was=was, wo=wo, category=cat, page=page_num)
        df = df_from_page(url)
        df_list.append(df)
        print('fetched {} entries'.format(df.shape[0]))

    df_all = pd.concat(df_list, axis=0, join='outer', ignore_index=True, sort=True)
    df_all.sort_values(by='Bezeichnung', inplace=True)
    print('fetched total of {} entries'.format(df_all.shape[0]))
    # This is not suited to be displayed in the browser unless converted to string
    # df_all['query'] = [query_dict for i in range(df_all.shape[0])]
    df_all['query'] = pd.Series([str(query_dict) for i in range(df_all.shape[0])]).astype('category')
    # df_all['query'] = df_all['query'].apply(lambda x: x.astype('category'))
    return df_all
