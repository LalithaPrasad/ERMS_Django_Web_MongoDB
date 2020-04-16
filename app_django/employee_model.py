from app_django import mongo

class Employee(object):

    def __init__(self, n, a, e, r):
        self.name=n
        self.age=a
        self.ed=e
        self.role=r

    def to_dict(self):
        fields=['name','age','ed','role']
        return dict(zip(fields,[self.name,self.age,self.ed,self.role]))

    def save(self):
        if mongo.collection.count() == 0:
            id = 0
        else:
            tmp = mongo.collection.find().sort("_id", -1).limit(1)
            tmp1 = tmp.next()
            id = int(tmp1['_id'])
        emp = self.to_dict()
        emp['_id'] = int(id)+1
        mongo.collection.insert_one(emp)

    @staticmethod
    def delete(id):
        query = {"_id" : id}
        mongo.collection.delete_one(query)

    @staticmethod
    def update(id, values):
        query = {"_id" : id}
        data = {"$set" : values}
        mongo.collection.update_one(query, data)

    @staticmethod
    def all():
        tmp = mongo.collection.find()
        fields = ('name', 'age', 'ed', 'role')
        emp = []
        tmp1 = {}
        for elmt in tmp:
            for f in fields:
                tmp1[f] = elmt[f]
            tmp1['id'] = elmt['_id']
            emp.append(tmp1)
            tmp1 = {}
        return emp
