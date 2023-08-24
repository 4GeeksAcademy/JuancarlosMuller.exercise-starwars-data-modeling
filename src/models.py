import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime 
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False,unique=True)
    password = Column(String(250), nullable=False)
    suscription_date= Column(DateTime, nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name= Column(String(250))
    specie = Column(String(250))
    gender = Column(String(250), nullable=False)
    heigth = Column(Integer)
    weight= Column(Integer)

    

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name= Column(String(250))
    weather = Column(String(250))
    land = Column(String(250), nullable=False)
    population = Column(Integer)
 
class Favorite (Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship("User")
    planet = relationship("Planet")
    character = relationship("Character")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
