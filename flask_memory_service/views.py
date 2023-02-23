from bson import ObjectId
from flask import jsonify, request, abort
from flask_restful import Resource

from app import db


class ApiIndex(Resource):
    def get(self):
        """Retrieve all records from the database"""
        data = db.api.find()
        new = [i for i in data]
        return jsonify(new)

    def post(self):
        """Creating a database entry"""
        insert_data = request.form.to_dict()
        if bool(insert_data) is True:
            id_create_obj = db.api.insert_one(insert_data)
            create_obj = db.api.find_one({"_id": id_create_obj.inserted_id})
            return jsonify(create_obj)
        abort(404, description="Arguments not found")


class ApiPut(Resource):
    def put(self, id_key):
        """
        Changing a database entry
         id_key is the _id in the database
        """
        new_value = dict.fromkeys(["value_used"], request.json["value_used"])
        data = db.api.find_one_and_update(
            {"_id": ObjectId(id_key)}, update={"$set": new_value}
        )

        return jsonify(data)
