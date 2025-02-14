from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Text, Integer,String, VARCHAR, TIMESTAMP, BOOLEAN, Float, DateTime

class ServiceBase:

    def __init__(self, T:type, engine):
        self.T = T
        self.engine = engine
        self.db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    def  getAll(self)->list:
        listdata=self.db_session.query(self.T).all()
        return listdata
    
    def getById(self,id):
        data=self.db_session.get(self.T,id)
        return data
    
    def add(self,data)->bool:
        try:
            self.db_session.add(data)
            self.db_session.commit()
            return True
        except:
            self.db_session.rollback()
            return False
        
    def update(self,data)->bool:
        try:
            self.db_session.merge(data)
            self.db_session.commit()
            return True
        except:
            self.db_session.rollback()
            return False

    def delete(self,id)->bool:
        try:
            data=self.getById(id)
            self.db_session.delete(data)
            self.db_session.commit()
            return True
        except:
            self.db_session.rollback()
            return False

