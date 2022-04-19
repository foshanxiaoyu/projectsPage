from fastapi import APIRouter
from bson import  ObjectId
# from models.user import (User,UpdateUserModel,ResponseModel,ErrorResponseModel)
from config.db import conn,user_info
from models.user import User
from schemas.userSchema import userEntity,usersEntity,serializeDict,serializeList
 
uroute = APIRouter() 

@uroute.get('/')
async def find_all_users():
    return serializeList(user_info.find())
    # return serializeList(conn.fastDB.user_info.find())

# @uroute.get('/')
# async def find_all_u():
#     print(conn.fastDB.user_info.find())
#     print(usersEntity(conn.fastDB.user_info.find()))
#     return usersEntity(conn.fastDB.user_info.find())
  
# @uroute.post('/')
# async def create_user(user:User):
#     result = await conn.fastDB.user_info.insert_one(dict(user))
#     return userEntity(conn.fastDB.user_info.find())

@uroute.post('/')
async def create_user(user: User):
    user_info.insert_one(dict(user))
    return serializeList(user_info.find())


@uroute.put('/{id}')
async def update_user(id,user: User):
    user_info.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(user_info.find_one({"_id":ObjectId(id)}))

@uroute.delete('/{id}')
async def delete_user(id,user: User):
    return serializeDict(user_info.find_one_and_delete({"_id":ObjectId(id)}))