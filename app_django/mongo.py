from pymongo import MongoClient

class MongoDB(object):

    def __init__(self, db_name, col_name):
        con = MongoClient("mongodb://localhost:27017/")
        db = con[db_name]
        self.collection = db[col_name]
        return
