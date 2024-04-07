from pymongo import MongoClient

# const uri = "mongodb://user:<password>@foshanxxxxxx.com:[port]/"
# 这个地方如果不加<,authSource="admin"> 自已的mongodb巨坑


conn = MongoClient('mongodb://use:<password>@foshanxxxxxx.com:[prot]/fastDB' ,authSource="admin")

# Create a new database.
# use(database)

# Create a new collection.
# db.createCollection(collection)
# import motor.motor_asyncio

# MONGO_DETAILS = "mongodb://localhost:27017"

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = conn.fastDB

user_info = database.get_collection("user_info")


# helpers


# def student_helper(user) -> dict:
#     return {
#         "id": str(user["_id"]),
#         "name": user["name"],
#         "email": user["email"],
#         "password": user["password"],
#     }
