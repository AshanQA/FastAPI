from src.config.database import Base
from fastapi import Depends, FastAPI
from pydantic import model_serializer
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.config.database import engine
from src.schemas import UserSchema
from src.models import Address, User


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def root():
    return {"test":"This is a test"}

@app.post('/user')
def create_user(user:UserSchema, db:Session = Depends(get_db)):  
    new_user = User(id = user.id,first_name = user.first_name, last_name = user.last_name, email = user.email, address_id = user.address_id, address = user.address)
    new_address = Address(adress_id = user.address_id,address = user.address, users = [new_user])
    db.add(new_user)
    db.add(new_address)
    db.commit()
    db.refresh(new_user)
    return new_user
