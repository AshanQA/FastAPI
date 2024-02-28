from pydantic import BaseModel

class UserSchema(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    address_id:int
    address:str

class AdressSchema(BaseModel):
    address_id:int
    adress:str