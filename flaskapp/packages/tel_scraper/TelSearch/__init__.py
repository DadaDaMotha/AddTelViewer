from .model import db_cols
from .. import utils
import pandas as pd
import re
from urllib.parse import quote_plus as urlquote

'''
Tel Search Limits the number of pages to 20.
'''

max_pages = 20
entries_per_page = 10


def get_entry_count(page):
    '''

    :param page: parsed html from page from bs4
    :return: how many search results are there for the query
    '''

    tmp = page.header.h1
    if tmp:
        entries_info = tmp.text
    else:
        return 1
    # total_entries = re.search(r"^\d+", entries_info)[0]
    entry_count = re.search(r"^\s*(\d+)", entries_info).group(1)
    return entry_count

def generate_search_url(was='', wo='', category=None, page=None):
    '''

    :param was: Nach was gesucht wird
    :param wo: Wo gesucht wird
    :param category: Firmen, Private oder nichts (sucht beides)
    :return: url string

    Der website mit pages=12 entält ALLE Einträge bis page 12
    '''

    mapping = {
        'Private': 'privat',
        'Firmen': 'firma'
    }

    url = 'https://tel.search.ch/?'


    if was:
        url += 'was={}'.format(urlquote(was))

    if wo:
        if not url.endswith('?'):
            url += '&wo={}'.format(urlquote(wo))
        else:
            url += 'wo={}'.format(urlquote(wo))

    if category in ['Private', 'Firmen']:
        if not url.endswith('?'):
            url += '&{}=1'.format(mapping[category])
        else:
            raise AssertionError('Wenistens Ort oder Bezeichnung muss angegeben werden!')

    if page:
        url += '&pages={}'.format(page)

    return url

def df_from_page(tel_search_url):
    ddict = {key: [] for key in db_cols}
    page = utils.get_one_page(tel_search_url)
    # result_count = page.h1

    ol = page.body.ol
    # Get a list of all table elements
    entries = ol.findAll("table", {'class': 'tel-resultentry'})

    for entry in entries:

        title = entry.h1.a.text
        cat = entry.find('div', {'class': 'tel-categories'}).text
        addr_block = entry.find('div', {'class': 'tel-address'})
        addr_tot = addr_block.text

        # addr_info = re.search(r"^\s*(\w+)\s*(\d+\w*)\s*", addr_tot)
        addr_info = re.search(r"\s*(\D*)(\d*-?\d*\w*)\s*,\s*(\d+\w*)\s(\w*)", addr_tot)
        if addr_info:
            street = addr_info.group(1)
            street_num = addr_info.group(2)
        else:
            print('Could not parse street and street num of {}'.format(title))
            print('Link: ', tel_search_url)
            print('Total Addr:', addr_tot)
            street = ''
            street_num = ''

        plz = addr_block.find('span', {'class': 'postal-code'}).text
        locality = addr_block.find('span', {'class': 'locality'}).text
        region = addr_block.find('span', {'class': 'region'}).text

        try:
            occupation = entry.find('div', {'class': 'tel-occupation'}).text
        except:
            occupation = ''

        # print(20 * '-')
        # print(title)
        # print(addr_tot)

        # this is sometimes also missing
        tel_nr_block = entry.find('div', {'class': 'tel-number'})

        if not tel_nr_block:
            print('No Div element tel-number for {}'.format(title))
            print('Link: ', tel_search_url)
            print('Total Addr:', addr_tot)
        else:
            tel_nr_subblock = tel_nr_block.findAll('a')
            try:
                werbung_jn = tel_nr_block.span.span.attrs['title']
            except:
                werbung_jn = ''
            if tel_nr_subblock:
                # Find at least the phone number
                tel_nr = tel_nr_subblock[0].text
                try:
                    website = tel_nr_subblock[1].attrs['href']
                except:
                    website = ''
            else:
                print('{} in {} has no phone number'.format(title, locality))
                tel_nr = ''
                website = ''

        ddict['Betriebsart'].append(occupation)
        ddict['Bezeichnung'].append(title)
        ddict['Hausnummer'].append(street_num)
        ddict['Kategorie'].append(cat)
        ddict['Ort'].append(locality)
        ddict['PLZ'].append(plz)
        ddict['Region'].append(region)
        ddict['Strasse'].append(street)
        ddict['Telefon'].append(tel_nr)
        ddict['URL'].append(tel_search_url)
        ddict['Website'].append(website)
        ddict['Werbung'].append(werbung_jn)

    df = pd.DataFrame(data=ddict)
    return df

def page_aggregator(query_dict, max_pages=max_pages):
    '''
    :param query_dict: Enthält
        was: Bezeichchung für beschreibung
        wo: Ortsbezeichnung
        category: Firmen, Private, Alles
    :return: concatenated df from all the pages
    '''
    print(40*'-')
    print('executing page aggregator')
    was = query_dict['was']
    wo = query_dict['wo']
    cat = query_dict['category']
    print('Query:')
    print('-was:', was)
    print('-wo:', wo)
    print('-cat:', cat)

    if not was and not wo:
        raise AssertionError('Leere Suchanfrage!')

    # create initial url
    url_initial = generate_search_url(was=was, wo=wo, category=cat)
    page = utils.get_one_page(url_initial)
    entry_count = get_entry_count(page)
    print('Total Number of search results: ', entry_count)

    loops = utils.calculate_loops(entries_per_page, entry_count)
    print('pages: ', loops)
    # df_initial = df_from_page(url_initial)

    # df_list.append(df_initial)
    # print('fetched {} entries'.format(df_initial.shape[0]))

    if max_pages:
        if max_pages < loops:
            print('Setting to max. {} pages'.format(max_pages))
            loops = max_pages

    # for page_num in range(2, loops+1):
    #     print('loop: ', page_num)
    #     url = generate_search_url(was=was, wo=wo, category=cat, page=page_num)
    #     df = df_from_page(url)
    #     df_list.append(df)

        # print('fetched {} entries'.format(df.shape[0]))

    url = generate_search_url(was=was, wo=wo, category=cat, page=loops)
    df_all = df_from_page(url)

    print('fetched entries of final df: ', df_all.shape[0])

    # df_all = pd.concat(df_list, axis=0, join='outer', ignore_index=True, sort=True)

    df_all.sort_values(by='Bezeichnung', inplace=True)
    df_all['query'] = pd.Series([str(query_dict) for i in range(df_all.shape[0])]).astype('category')

    return df_all
