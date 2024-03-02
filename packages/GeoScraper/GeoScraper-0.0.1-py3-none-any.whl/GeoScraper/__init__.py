'''
geoscraper

https://wiki.openstreetmap.org/wiki/API
https://wiki.openstreetmap.org/wiki/OSM_XML/XSD
https://wiki.openstreetmap.org/wiki/Map_features
'''

import os
import requests
from copy import deepcopy
from typing import Union
from urllib.parse import urlparse

import xmltodict


class GeoScraper_Path_Exception(Exception):
    pass


class GeoScraper_File_Exception(Exception):
    pass


class GeoScraper_URL_Exception(Exception):
    pass


class GeoScraper_Node_Exception(Exception):
    pass


class OSM_URL_Wizard(object):
    def __init__(self,
                 api_ver: Union[str, float] = '0.6'):
        self.api_ver = api_ver
    
    def api_version_url(self) -> str:
        return r'https://api.openstreetmap.org/api/versions'
    
    def capabilities_url(self) -> str:
        return r'https://api.openstreetmap.org/api/capabilities'
    
    def bbox_url(self,
                 left:   Union[float, str],
                 bottom: Union[float, str],
                 right:  Union[float, str],
                 top:    Union[float, str]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/map?bbox={left},{bottom},{right},{top}'.format(api_ver = self.api_ver,
                                                                                                            left    = left,
                                                                                                            bottom  = bottom,
                                                                                                            right   = right,
                                                                                                            top     = top)
    
    def permissions_url(self) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/permissions'.format(api_ver = self.api_ver)
    
    def get_node_url(self,
                     id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/node/{id}'.format(api_ver = self.api_ver,
                                                                               id      = id)
    
    def get_way_url(self,
                    id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/way/{id}'.format(api_ver = self.api_ver,
                                                                              id      = id)
    
    def get_relation_url(self,
                         id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/relation/{id}'.format(api_ver = self.api_ver,
                                                                                   id      = id)
    
    def get_node_history_url(self,
                             id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/node/{id}/history'.format(api_ver = self.api_ver,
                                                                                       id      = id)
    
    def get_way_history_url(self,
                            id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/way/{id}/history'.format(api_ver = self.api_ver,
                                                                                      id      = id)
    
    def get_relation_history_url(self,
                                 id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/relation/{id}/history'.format(api_ver = self.api_ver,
                                                                                           id      = id)
    
    def get_node_version_url(self,
                             id:      Union[str, int],
                             version: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/node/{id}/{version}'.format(api_ver = self.api_ver,
                                                                                         id      = id,
                                                                                         version = version)
    
    def get_way_version_url(self,
                            id:      Union[str, int],
                            version: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/way/{id}/{version}'.format(api_ver = self.api_ver,
                                                                                        id      = id,
                                                                                        version = version)
    
    def get_relation_version_url(self,
                                 id:      Union[str, int],
                                 version: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/relation/{id}/{version}'.format(api_ver = self.api_ver,
                                                                                             id      = id,
                                                                                             version = version)
    
    def get_nodes_url(self,
                      ids: list[Union[str, int]]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/nodes?{ids}'.format(api_ver = self.api_ver,
                                                                                 ids     = ','.join(ids))
    
    def get_ways_url(self,
                     ids: list[Union[str, int]]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/ways?{ids}'.format(api_ver = self.api_ver,
                                                                                ids     = ','.join(ids))
    
    def get_relations_url(self,
                          ids: list[Union[str, int]]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/relations?{ids}'.format(api_ver = self.api_ver,
                                                                                     ids     = ','.join(ids))
    
    def get_node_relations_url(self,
                               id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/node/{id}/relations'.format(api_ver = self.api_ver,
                                                                                         id      = id)
    
    def get_way_relations_url(self,
                              id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/way/{id}/relations'.format(api_ver = self.api_ver,
                                                                                        id      = id)
    
    def get_relation_relations_url(self,
                                   id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/relation/{id}/relations'.format(api_ver = self.api_ver,
                                                                                             id      = id)
    
    def get_ways_for_node_url(self,
                              id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/node/{id}/ways'.format(api_ver = self.api_ver,
                                                                                    id      = id)
    
    def get_way_full_data_url(self,
                              id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/way/{id}/full'.format(api_ver = self.api_ver,
                                                                                   id      = id)
    
    def get_relation_full_data_url(self,
                                   id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/relation/{id}/full'.format(api_ver = self.api_ver,
                                                                                        id      = id)
    
    def get_user_details_url(self,
                             id: Union[str, int]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/user/{id}'.format(api_ver = self.api_ver,
                                                                               id      = id)
    
    def get_users_details_url(self,
                              ids: list[Union[str, int]]) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/users?users={ids}'.format(api_ver = self.api_ver,
                                                                                       ids     = ','.join(ids))
    
    def get_your_details_url(self) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/user/details'.format(api_ver = self.api_ver)
    
    def get_your_preferences_url(self) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/user/preferences'.format(api_ver = self.api_ver)
    
    def get_your_preference_url(self,
                                preference: str) -> str:
        return r'https://api.openstreetmap.org/api/{api_ver}/user/preferences/{preference}'.format(api_ver    = self.api_ver,
                                                                                                   preference = preference)


class OSM_XML(object):
    def __init__(self) -> None:
        self.__xml = ''
        self.__clear_datasets()
    
    def __clear_datasets(self) -> None:
        self.__raw_data         = {}
        self.__data             = {}
        self.__Aerialway        = []
        self.__Aeroway          = []
        self.__Amenity          = []
        self.__Barrier          = []
        self.__Boundary         = []
        self.__Building         = []
        self.__Craft            = []
        self.__Emergency        = []
        self.__Geological       = []
        self.__Healthcare       = []
        self.__Highway          = []
        self.__Historic         = []
        self.__Landuse          = []
        self.__Leisure          = []
        self.__Man_made         = []
        self.__Military         = []
        self.__Natural          = []
        self.__Office           = []
        self.__Place            = []
        self.__Power            = []
        self.__Public_transport = []
        self.__Railway          = []
        self.__Route            = []
        self.__Shop             = []
        self.__Sport            = []
        self.__Telecom          = []
        self.__Tourism          = []
        self.__Water            = []
        self.__Waterway         = []
    
    def set_xml(self,
                xml: str) -> None:
        self.__xml = xml
    
    def __parse_file(self) -> None:
        self.__raw_data = xmltodict.parse(self.__xml)
    
    def __link_nd_tag(self,
                      node_id: str) -> dict:
        try:
            match_idx = self.__node_keys.index(node_id)
            return self.__nodes[match_idx]
        except ValueError:
            self.__clear_datasets()
            raise GeoScraper_Node_Exception('Could not find a matching node with ID: {}'.format(node_id))
    
    def __link_data(self) -> None:
        if 'osm' not in self.__raw_data.keys():
            self.__clear_datasets()
            raise GeoScraper_File_Exception('Invalid file - \'osm\' element not found')
        
        try:
            self.__nodes     = self.__raw_data['osm']['node']
            self.__node_keys = [node[key] for node in self.__nodes for key in node if key == '@id']
        except KeyError:
            self.__clear_datasets()
            raise GeoScraper_Node_Exception('No nodes found in file')
        
        self.__data_types = [key for key in self.__raw_data['osm'].keys() if not key.startswith('@')]
        self.__data       = deepcopy(self.__raw_data['osm'])
        
        to_pop = []
        
        for key in self.__data:
            if key not in self.__data_types:
                to_pop.append(key)
        
        for key in to_pop:
            self.__data.pop(key, None)
        
        for element_name in self.__data_types:
            element = self.__data[element_name]
            
            if (element_name == 'node') or (element is dict):
                continue
            
            for feature_num, feature in enumerate(element):
                if type(feature) is not dict:
                    continue
                
                orig_feat_keys = feature.keys()
                
                for key in orig_feat_keys:
                    if type(feature[key]) == list:
                        self.__data[element_name][feature_num][key] = compress_dicts(feature[key])
                
                if 'nd' not in feature.keys():
                    continue
                
                matching_node_data = [self.__link_nd_tag(nd_ref) for nd_ref in feature['nd']['@ref']]
                self.__data[element_name][feature_num]['node'] = matching_node_data
    
    def __sort_ways(self) -> None:
        elements = []
        
        if 'way' in self.__data.keys():
            elements.extend(self.__data['way'])
        
        if 'node' in self.__data.keys():
            elements.extend(self.__data['node'])
        
        for element in elements:
            if 'tag' not in element.keys():
                continue
            
            if type(element['tag']) is list:
                element['tag'] = compress_dicts(element['tag'])
            
            element_keys     = element.keys()
            element_tag_keys = element['tag']['@k']

            node_ids = []
            
            if 'nd' in element_keys:
                node_ids = element['nd']['@ref']
            
            tags     = element['tag']
            tag_keys = tags['@k']
            tag_vals = tags['@v']
            tags     = list(zip(tag_keys, tag_vals))
            
            lats = []
            lons = []
            
            if 'node' in element_keys:
                for node in element['node']:
                    lats.append(node['@lat'])
                    lons.append(node['@lon'])
                    
            elif ('@lat' in element_keys) and ('@lon' in element_keys):
                lats.append(element['@lat'])
                lons.append(element['@lon'])
            
            coords = list(zip(lons, lats))
            
            entry = {'id':        element['@id'],
                     'uid':       element['@uid'],
                     'timestamp': element['@timestamp'],
                     'node_ids':  node_ids,
                     'tag_keys':  tag_keys,
                     'tag_vals':  tag_vals,
                     'tags':      tags,
                     'lats':      lats,
                     'lons':      lons,
                     'coords':    coords}
            
            if 'aerialway' in element_tag_keys:
                self.__Aerialway.append(entry)
            
            if 'aeroway' in element_tag_keys:
                self.__Aeroway.append(entry)
            
            if 'amenity' in element_tag_keys:
                self.__Amenity.append(entry)
            
            if 'barrier' in element_tag_keys:
                self.__Barrier.append(entry)
            
            if 'boundary' in element_tag_keys:
                self.__Boundary.append(entry)
            
            if 'building' in element_tag_keys:
                self.__Building.append(entry)
            
            if 'craft' in element_tag_keys:
                self.__Craft.append(entry)
            
            if 'emergency' in element_tag_keys:
                self.__Emergency.append(entry)
            
            if 'geological' in element_tag_keys:
                self.__Geological.append(entry)
            
            if 'healthcare' in element_tag_keys:
                self.__Healthcare.append(entry)
            
            if 'highway' in element_tag_keys:
                self.__Highway.append(entry)
            
            if 'historic' in element_tag_keys:
                self.__Historic.append(entry)
            
            if 'landuse' in element_tag_keys:
                self.__Landuse.append(entry)
            
            if 'leisure' in element_tag_keys:
                self.__Leisure.append(entry)
            
            if 'man_made' in element_tag_keys:
                self.__Man_made.append(entry)
            
            if 'military' in element_tag_keys:
                self.__Military.append(entry)
            
            if 'natural' in element_tag_keys:
                self.__Natural.append(entry)
            
            if 'office' in element_tag_keys:
                self.__Office.append(entry)
            
            if 'place' in element_tag_keys:
                self.__Place.append(entry)
            
            if 'power' in element_tag_keys:
                self.__Power.append(entry)
            
            if 'public_transport' in element_tag_keys:
                self.__Public_transport.append(entry)
            
            if 'railway' in element_tag_keys:
                self.__Railway.append(entry)
            
            if 'route' in element_tag_keys:
                self.__Route.append(entry)
            
            if 'shop' in element_tag_keys:
                self.__Shop.append(entry)
            
            if 'sport' in element_tag_keys:
                self.__Sport.append(entry)
            
            if 'telecom' in element_tag_keys:
                self.__Telecom.append(entry)
            
            if 'tourism' in element_tag_keys:
                self.__Tourism.append(entry)
            
            if 'water' in element_tag_keys:
                self.__Water.append(entry)
            
            if 'waterway' in element_tag_keys:
                self.__Waterway.append(entry)
    
    def parse(self,
              xml: str=None) -> dict:
        self.__clear_datasets()
        
        if xml is not None:
            self.set_xml(xml)
        
        self.__parse_file()
        self.__link_data()
        self.__sort_ways()
        
        return self.__data
    
    def raw_data(self) -> dict:
        return self.__raw_data
    
    def data(self) -> dict:
        return self.__data
    
    def nodes(self) -> dict:
        return self.__data['node']
    
    def ways(self) -> dict:
        return self.__data['way']
    
    def relations(self) -> dict:
        return self.__data['relation']
    
    def aerialways(self) -> list[dict]:
        return self.__Aerialway

    def aeroways(self) -> list[dict]:
        return self.__Aeroway

    def amenities(self) -> list[dict]:
        return self.__Amenity

    def barriers(self) -> list[dict]:
        return self.__Barrier

    def boundaries(self) -> list[dict]:
        return self.__Boundary

    def buildings(self) -> list[dict]:
        return self.__Building

    def crafts(self) -> list[dict]:
        return self.__Craft

    def emergency_locations(self) -> list[dict]:
        return self.__Emergency

    def geological_locations(self) -> list[dict]:
        return self.__Geological

    def healthcare_locations(self) -> list[dict]:
        return self.__Healthcare

    def highways(self) -> list[dict]:
        return self.__Highway

    def historic_locations(self) -> list[dict]:
        return self.__Historic

    def landuse(self) -> list[dict]:
        return self.__Landuse

    def leisure_locations(self) -> list[dict]:
        return self.__Leisure

    def man_made_locations(self) -> list[dict]:
        return self.__Man_made

    def military_locations(self) -> list[dict]:
        return self.__Military

    def natural_locations(self) -> list[dict]:
        return self.__Natural

    def offices(self) -> list[dict]:
        return self.__Office

    def places(self) -> list[dict]:
        return self.__Place

    def power_locations(self) -> list[dict]:
        return self.__Power

    def public_transport_locations(self) -> list[dict]:
        return self.__Public_transport

    def railways(self) -> list[dict]:
        return self.__Railway

    def routes(self) -> list[dict]:
        return self.__Route

    def shops(self) -> list[dict]:
        return self.__Shop

    def sport_locations(self) -> list[dict]:
        return self.__Sport

    def telecom_locations(self) -> list[dict]:
        return self.__Telecom

    def tourism_locations(self) -> list[dict]:
        return self.__Tourism

    def water_locations(self) -> list[dict]:
        return self.__Water

    def waterways(self) -> list[dict]:
        return self.__Waterway


class GeoScraper(OSM_URL_Wizard, OSM_XML):
    def __init__(self,
                 api_ver: Union[str, float] = '0.6'):
        super().__init__(api_ver)
    
    def from_str(self,
                 xml_text: str) -> dict:
        return self.parse(xml_text)
    
    def from_file(self,
                  path: str) -> dict:
        if not os.path.exists(path):
            raise GeoScraper_File_Exception('File does not exist')
        
        with open(path, 'r') as xml:
            xml_text = xml.read()
        
        return self.from_str(xml_text)
    
    def from_url(self,
                 url: str) -> dict:
        if not uri_validator(url):
            raise GeoScraper_URL_Exception('URL is invalid')
        
        r = requests.get(url)
        
        if not r.ok:
            raise GeoScraper_URL_Exception('URL Request Error Code: {}\n{}'.format(r.status_code,
                                                                                   r.text))
        
        return self.from_str(r.text)
    
    def from_bbox(self,
                  left:   Union[float, str],
                  bottom: Union[float, str],
                  right:  Union[float, str],
                  top:    Union[float, str]) -> dict:
        
        url = self.bbox_url(left,
                            bottom,
                            right,
                            top)
        
        if not uri_validator(url):
            raise GeoScraper_URL_Exception('URL is invalid')
        
        r = requests.get(url)
        
        if not r.ok:
            raise GeoScraper_URL_Exception('URL Request Error Code {}'.format(r.status_code))
        
        return self.from_str(r.text)
    

def uri_validator(x: str) -> bool:
    '''
    https://stackoverflow.com/a/38020041/9860973
    '''
    
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False

def compress_dicts(dict_list: list[dict]) -> Union[dict, list[dict]]:
    compress = True
    ref_keys = dict_list[0].keys()
    
    for dict in dict_list:
        if not dict.keys() == ref_keys:
            compress = False
            break
    
    if compress:
        compressed = {}
        
        for dict in dict_list:
            for key, value in dict.items():
                if key not in compressed.keys():
                    compressed[key] = []
                compressed[key].append(value)
        
        return compressed
    
    else:
        return dict_list