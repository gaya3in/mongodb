import pymongo
from bson.objectid import ObjectId

def connect_mongodb(action, id, emp_dict):
    my_client = pymongo.MongoClient("mongodb://myUserAdmin:123456@localhost:27017/?authMechanism=DEFAULT")
    db_name = my_client["test"]
    collection_name = db_name["mongodb_employee"]

    if action == "read":
        emp_details = collection_name.find({})
        return emp_details
    elif action == "create":
        emp_dict["_id"] = ObjectId()
        print(emp_dict)
        collection_name.insert(emp_dict)
    elif action == "get":
        emp_details = collection_name.find_one({"_id": ObjectId(id)})
        return emp_details
    elif action == "update":
        print("Before update")
        print(emp_dict)
        collection_name.update_one({"_id": ObjectId(id)}, {"$set": emp_dict})
        print("After update")
    elif action == "delete":
        collection_name.delete_one({"_id": ObjectId(id)})

