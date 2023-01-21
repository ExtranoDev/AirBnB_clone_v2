#!/usr/bin/python3
"""Script defines class for database storage engine"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """query"""
        dict_res = dict()
        if cls is not None:
            cls = eval(cls)
            obj_ins = self.__session.query(cls).all()
            for obj in obj_ins:
                key = '.'.join([obj.__class__.__name__, obj.id])
                dict_res[key] = obj
        else:
            all_cls = [BaseModel, User, State, City, Amenity, Place, Review]
            for cls in all_cls:
                obj_ins = self.__session.query(cls).all()
                for obj in obj_ins():
                    key = '.'.join([obj.__class__.__name__, obj.id])
                    dict_res[key] = obj
        return (dict_res)

    def new(self, obj):
        """add object to current databse session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables and session in the database"""
        self.__session = Base.metadata.create_all(self.__engine)
        make_sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(make_sess)
        self.__session = Session()


    def close(self):
        """Closes session"""
        self.__session.close()
