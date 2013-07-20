'''
Created on Sep 30, 2012

@author: xiaoxiao
'''
from pymongo import Connection
import numpy

class DataSource(object):
    '''
    classdocs
    '''
    db = None

    def __init__(self):
        '''
        Constructor
        '''
        self.db = Connection().PW_2012_09_02_09_03_35
        self.another_db = Connection().programmable_web

    def get_member_mashups_collections(self):
        member_mashups = self.another_db.member_mashup.find()
        return [member_mashup for member_mashup in member_mashups]

    def search_api(self, key):
        apis = self.db.apis.find({"description": {"$regex": key}})
        return [api for api in apis]

    def search_mashup(self, key):
        mashups = self.db.mashups.find({"description": {"$regex": key}})
        return [mashup for mashup in mashups]

    def mashup_with_apis(self):
        pairs = self.pairs()
        mashup_map = {}
        for pair in pairs:
            if mashup_map.get(pair["mashup"]) == None:
                mashup_map[pair["mashup"]] = []
            mashup_map[pair["mashup"]].append(pair["api"])
        return mashup_map

    def api_with_mashups(self):
        pairs = self.pairs()
        api_map = {}
        for pair in pairs:
            if api_map.get(pair["api"]) == None:
                api_map[pair["api"]] = []
            api_map[pair["api"]].append(pair["mashup"])
        return api_map

    def apis(self):
        apis = self.db.apis.find()
        return [api for api in apis]
    
    def mashups(self):
        mashups = self.db.mashups.find()
        return [mashup for mashup in mashups]

    def pairs(self):
        pairs = self.db.pairs.find()
        return [pair for pair in pairs]
    
    def publications(self):
        publications = self.db.publication.find()
        return [publication for publication in publications]

    def api_by_id(self, _id):
        apis = self.db.apis.find({"id": _id})
        result = [api for api in apis]
        if result:
            return result[0]

    def mashup_by_id(self, _id):
        mashups = self.db.mashups.find({"id": _id})
        result = [mashup for mashup in mashups]
        if result:
            return result[0]

    def mashups_by_api(self, api):
        pairs = self.db.pairs.find({"api": api["id"]})
        mashups = []
        for pair in pairs:
            mashups.extend([mashup for mashup in self.db.mashups.find({"id": pair["mashup"]})])
        return mashups

    def apis_by_mashup(self, mashup):
        pairs = self.db.pairs.find({"mashup": mashup["id"]})
        apis = []
        for pair in pairs:
            apis.extend([api for api in self.db.apis.find({"id": pair["api"]})])
        return apis

    def apis_by_category(self, category):
        apis = self.db.apis.find({"category": category})
        return [api for api in apis]

    def get_publication_author_matrix(self):
        publications = self.publications()
        author_map = {}
        author_count = 0
        for (counter, publication) in enumerate(publications):
            for author in publication["author"]:
                if author_map.get(author) == None:
                    author_map[author] = author_count
                    author_count += 1
        matrix = numpy.zeros((len(publications), len(author_map)))
        for (counter, publication) in enumerate(publications):
            for author in publication["author"]:
                author_id = author_map.get(author)
                matrix[counter][author_id] = 1
        return matrix
