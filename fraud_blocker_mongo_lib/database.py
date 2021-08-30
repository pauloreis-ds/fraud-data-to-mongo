import pymongo


class MongoDB:
    def __init__(self, database='mydb', client="mongodb://localhost:27017/"):
        self.client = pymongo.MongoClient(client)
        self.db = self.client[database]
        self.collections = {}

    def add_collection(self, collection):
        self.collections[collection] = self.db[collection]
        return self

    def drop_collection(self, collection):
        self.db[collection].drop()
        return self

    def drop_collections(self, collections):
        for collection in collections:
            self.db[collection].drop()
        return self

    def databases(self):
        return self.client.list_database_names()

    def collection(self, collection):
        if collection in self.collections:
            return self.collections[collection]
        else:
            self.add_collection(collection)
            return self.collections[collection]

    def collection_names(self):
        return self.db.list_collection_names()
