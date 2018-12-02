# configuration file for Object-Relational Management

import sys #provides functions and modules used to manipulate different Python runtime environment

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base #used in configuration and class codes

from sqlalchemy.orm import relationship #allow you to create foreign key relationships etc.

from sqlalchemy import create_engine

Base = declarative_base() #create an instance for declarative_base() class

####### insert at the end of file #######

engine = create_engine(
'sqlite:///restaurantmenu.db' #point to the database we'll use
)

Base.metadata.create_all(engine) #goes to the db and pack the classes we will create as new tables in our db
