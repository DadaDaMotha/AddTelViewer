import json


def JSON_write(config, to_file):

    with open(to_file, 'w') as f:
        json.dump(config, f)


def JSON_update(config, to_file):

    with open(to_file, 'a') as f:
        json.dump(config, f)


def JSON_read(from_file):

    with open(from_file, 'r') as f:
        config = json.load(f)
        f.close()
        return config


def func_name():
    import traceback
    return traceback.extract_stack(None, 2)[0][2]


def read_file_as_str(filepath):
    with open(filepath) as f:
        res = f.read()
    return res


def add_mmqgis_fields(df):
    '''

    :param df: take in a dataframe from page_aggregator function of LocalCH or TelSearch
    :return: re-arranged dataframe with different columns headers and collapsed address

    Specs: needs address, city, state, country
    mmqgis working examples:

        Rautistrasse 33 | Zuerich | Zuerich |	Schweiz
        Rautistrasse 33 | 8047 Zuerich | Zuerich |	Schweiz

    '''

    dff = df.copy(deep=True)
    dff['address'] = df[['Strasse', 'Hausnummer']].apply(lambda x: ' '.join(x), axis=1)
    dff['city'] = df[['PLZ', 'Ort']].apply(lambda x: ' '.join(x), axis=1)
    dff['country'] = 'Schweiz'
    return dff
