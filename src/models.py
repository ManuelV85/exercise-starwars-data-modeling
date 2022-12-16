import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    password = Column(String(10), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(50), nullable = False)

class Character(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(100), nullable=False)

class Ships(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    ships_name = Column(String(100), nullable=False)


class Planet_Favorite(Base):
    __tablename__='planet_favorite'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship(Account)
    planet_id= Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

  
class Character_favorite(Base):
    __tablename__='character_favorite'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship(Account)
    character_id= Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)


class Ships_favorite(Base):
    __tablename__='ships_favorite'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship(Account)
    ships_id= Column(Integer, ForeignKey('ships.id'))
    ships = relationship(Ships)


def to_dict(self):
        return {}   



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
