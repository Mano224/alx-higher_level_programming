#!/usr/bin/python3
# python file that contains the class definition of a State and an instance Base = declarative_base()

from sqlalchemy import Column, Integer, CHAR, create_engine, String
from sqlalchemy.ext.declarative import declarative_base
import sys
Base = declarative_base()

if __name__ == '__main__':
    mysql_url = f"mysql+mysqlconnector://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/states"
    engine = create_engine(mysql_url, echo=True)
    Base.metadata.create_all(bind = engine)
    
    class State(Base):
        __tablename__ = "state"
        id = Column("id", Integer, autoincrement=True, primary_key=True, nullable=false, unique=True)
        name = column("name", String(128), nullable=False)
