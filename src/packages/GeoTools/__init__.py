from geopy.geocoders import Nominatim
import numpy as np
from .core import *

# class GeoLocator:
#     geolocator = Nominatim(user_agent="plz-search")
#
#     def __init__(self):
#         self.input = None
#         self.location = None
#         self.lat = None
#         self.long = None
#         self.addr = None
#         self.bound_box = None
#         self.type = None
#         self.class_type = None
#         self.map_obj_type = None
#
#     def set_default(self):
#         self.lat = 46.876387
#         self.long = 8.347498
#         self.addr = 'Wolfenschiessen'
#
#     def store_query(self, query):
#         if query:
#             self.input = query
#             self.location = self.geolocator.geocode(query)
#             self.handle_request()
#             self.info_print()
#         else:
#             self.set_default()
#
#     def handle_request(self):
#         if not self.location is None:
#             self.lat = self.location.latitude
#             self.long = self.location.longitude
#             self.addr = self.location.address
#             self.bound_box = self.location.raw['boundingbox']
#             self.type = self.location.raw['type']
#             self.class_type = self.location.raw['class']
#             self.map_obj_type = self.location.raw['osm_type']
#         else:
#             print("Retry, location search was not successfull")
#             self.set_default()
#
#     def boundbox_center(self, get="float"):
#         bbox = np.asarray(self.bound_box, dtype=np.float64)
#         lat_mean = bbox[:2].mean().rount(7)
#         long_mean = bbox[2:4].mean().round(7)
#         if get == 'float':
#             return lat_mean, long_mean
#         else:
#             return str(lat_mean), str(long_mean)
#
#     def info_print(self):
#         for k, v in self.__dict__.items():
#             print("var: {}\t\tval: {}".format(k, v))