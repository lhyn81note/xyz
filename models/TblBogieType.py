from models.__base__ import *
from libs.Bind.dtobase import DtoBase
from libs.Bind.observableCollection import ObservableCollection

class TblBogieType(declarative_base()):
    __tablename__ = 'TblBogieType'
    zxjxh = Column(String, primary_key=True)
    zxjgd = Column(Float)
    Jzt1hxwy = Column(Float)
    Jzt2hxwy = Column(Float)
    Jzt1kjcxwy = Column(Float)
    Jzt2kjcxwy = Column(Float)
    FullLoadK = Column(Float)
    Jzt1Kzl = Column(Float)
    Jzt2Kzl = Column(Float)
    Jzt1Mzl = Column(Float)
    Jzt2Mzl = Column(Float)
    FullLoadCount = Column(Integer)
    bakParam1 = Column(String)
    bakParam2 = Column(String)
    bakParam3 = Column(String)
    bakParam4 = Column(String)
    bakParam5 = Column(String)
    bakParam6 = Column(String)
    bakParam7 = Column(String)
    bakParam8 = Column(String)
    bakParam9 = Column(String)
    bakParam10 = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblBogieType.HandlerBase(TblBogieType, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblBogieType.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
