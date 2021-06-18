from flask_restful import Resource
from models.store import StoreModel
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

class Store(Resource):
    
    @jwt_required()
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(),200
        return {"Message":"Store not found"},404    


    @jwt_required()
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"Message":"Store with name {} already exists.".format(name)}
        
        store = StoreModel(name)
        try:
            store.save_to_db()  
        except:
            return {"message":"Error occurred while creating the store {}.".format(name)},500 
        return store.json(),200         

    @jwt_required()
    def delete(self,name):
        if StoreModel.find_by_name(name):
            store = StoreModel.find_by_name(name)
            store.delete_from_db()
        return {"Message":"Store Deleted"},200


class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {"Stores",[store.json() for store in StoreModel.query.all()]}    


