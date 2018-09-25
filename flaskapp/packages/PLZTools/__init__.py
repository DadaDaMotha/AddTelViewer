import numpy as np
import pandas as pd
from packages.utils import func_name
from packages.GeoTools import GeoLocator
import os


basedir = (os.path.dirname(os.path.abspath(__file__)))


class PLZLoader():
    __path = os.path.join(basedir, 'raw_data', 'plz_verzeichnis_v2.geojson')
    __path_alt_names = os.path.join(basedir, 'raw_data', 'alternative-ortsbezeichnungen-und-gebietsbezeichnungen_v2.json')

    def __init__(self, test_sample=True):
        self.init_class(test_sample)

    def init_class(self, test_sample):
        print("---", func_name(), "---")
        raw_df = pd.read_json(self.__path)
        if test_sample:
            self.df = pd.DataFrame(data=[raw_df.features[i]['properties'] for i in range(10)])
        else:
            self.df = pd.DataFrame(data=[raw_df.features[i]['properties'] for i in range(raw_df.features.shape[0])])
        # for col in self.df.columns:
        #     self.__setattr__(col, self.df.loc[:, col])

    def fill_point_loc(self, save=False):
        pass

    def get_Dash_PLZ_all_opts(self, loc_only=False):
        if loc_only:
            df = self.df[~self.df.geo_pint_2d.isna()]
        else:
            df = self.df

        # unique_plz = df.postleitzahl.unique()
        # names = []
        # for plz in unique_plz:
        #     dff = df[df.postleitzahl == plz]
        #     name = dff.ortbez18.iloc[0]
        #     names.append(name)

        unique_plz = df.postleitzahl
        names = df.ortbez18

        opts = [{'label':"{} - {}".format(x, y), 'value':'{}!!{}'.format(x, y)} for x, y in zip(unique_plz, names)]
        return opts



    def get_Dash_lat_lon_lists(self, value_str):
        print("---", func_name(), "---")


        l = value_str.split(sep='!!')
        plz = int(l[0])
        name = l[1]

        df = self.df


        dff = df[df.postleitzahl == plz]
        mask = ~dff.geo_point_2d.isna()
        loc_inds = [*dff.index[mask]]

        if not loc_inds:
            dff = df[df.ortbez18 == name]
            mask = ~dff.geo_point_2d.isna()
            loc_inds = [*dff.index[mask]]


        if not loc_inds:
            print("Plz has no location from Swisspost data, looking up {}".format(dff.ortbez18.iloc[0]))
            GL = GeoLocator()
            GL.store_query(dff.ortbez18.iloc[0])
            GL.info_print()
            lat = [str(GL.lat)]
            long = [str(GL.long)]
            print('lat: ', lat)
            print('long', long)
            return lat, long, [GL.addr]
        else:
            print('Locations from Post available for {}'.format(dff.loc[loc_inds[0], 'ortbez18']))
            lats = []
            longs = []
            names = []
            # info_print(dff.index)
            for ind in loc_inds:
                lats.append(str(dff.loc[ind, 'geo_point_2d']['lat']))
                longs.append(str(dff.loc[ind, 'geo_point_2d']['lon']))
                names.append("{} - {}".format(str(dff.loc[ind, 'postleitzahl']), str(dff.loc[ind, 'ortbez18'])))
            # locs is a list of dicts, we want two lists lat, long of string values
            print('lats: ', lats)
            print('longs', longs)
            return lats, longs, names

    def test_data_quality(self):
        print("---", func_name(), "---")

        df = self.df
        # Test how many are unique PLZ
        plz_un = df.postleitzahl.unique()
        loc_count_un = []
        locs = []
        for plz in plz_un:
            dff = df[df.postleitzahl == plz]
            mask = ~dff.geo_point_2d.isna()
            loc_inds = [*dff.index[mask]]
            if not loc_inds:
                loc_count_un.append(0)
                pass
            else:
                first_loc_ind = loc_inds[0]
                # info_print(dff.index)
                locs.append(dff.loc[first_loc_ind, 'geo_point_2d'])
                loc_count = np.sum(mask)
                loc_count_un.append(loc_count)


        # info_print(df.ortbez18[np.asarray(loc_count_un)].unique())
        # info_print(df.postleitzahl[np.asarray(loc_count_un)].unique())


        loc_count_un = pd.Series(loc_count_un)
        locs = pd.Series(locs)
        print('---Test Data Quality----')
        # info_print('Df index:', df.index)
        print('Total entries:', df.shape[0])
        print('Unique PLZ:', plz_un.shape[0])
        print('Extracted Locations for un PLZ:', locs.shape[0])
        print('PLZ that have no location', np.sum(loc_count_un == 0))

        print('Unique Names18:', df.ortbez18.unique().shape[0])
        print('Unique Names27:', df.ortbez27.unique().shape[0])
        print('PLZ that have 1 location', np.sum(loc_count_un == 1))
        print('PLZ that have 2 locations', np.sum(loc_count_un == 2))
        print('PLZ that have mor than 2 locations', np.sum(loc_count_un > 2))
        print('PLZ that have mor than 3 locations', np.sum(loc_count_un > 3))


    def get_df_by_PLZ(self, plz_list):
        print("---", func_name(), "---")

        # try:
        #     p_list = [np.int64(x) for x in plz_list]
        # except:
        #     info_print('somethings is wrong with plz number input')
        #     return {}
        df_filtered = self.df[self.df.postleitzahl.isin(plz_list)]

        return df_filtered