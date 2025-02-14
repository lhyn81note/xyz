from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

def GenDbEnging(dbpath:str):
    engine = create_engine(dbpath)
    return engine