# from typing import Optional
from pydantic  import BaseModel, EmailStr

class User(BaseModel):
    name:str 
    email:str
    password:str

    # name:str = Field(...)
    # email:EmailStr= Field(...)
    # password:str= Field(...)

    # class config:
    #     schema_extra={
    #         "example":{
    #             {
    #                 "name":"张三",
    #                 "email":"zhanshan@163.com",
    #                 "password":"123456"
    #             }
    #         }
    #     }

        
# class UpdateUserModel(BaseModel):
#     name: Optional[str]
#     email: Optional[EmailStr]
#     password: Optional[str]

#     class config:
#         schema_extra={
#             "example":{
#                 {
#                     "name":"张三",
#                     "email":"zhanshan@163.com",
#                     "password":"123456"
#                 }
#             }
#         }




# def ResponseModel(data, message):
#     return {
#         "data": [data],
#         "code": 200,
#         "message": message,
#     }


# def ErrorResponseModel(error, code, message):
#     return {"error": error, "code": code, "message": message}