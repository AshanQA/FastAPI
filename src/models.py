from sqlalchemy import ForeignKey, String, Integer, Column
from sqlalchemy.orm import relationship
from src.config.database import Base

class User(Base):
    __tablename__ = 'user'        

    id = Column(Integer, primary_key=True)    #id (primary key), first name, last name, email (unique), and address_id (foreign key to the Address entity).
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True)
    address_id = Column(Integer, ForeignKey('address.address_id'))
    #address_id = Column(int, ForeignKey"address.address_id",nullable=False)
    address = relationship("Address",back_populates="users")

class Address(Base):

    __tablename__ = 'address'             #address_id (primary key) and address text.

    address_id = Column(Integer, primary_key=True)
    adress = Column(String(255))
    users = relationship("User",back_populates="address")