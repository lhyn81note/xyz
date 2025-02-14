from models.__base__ import *
from libs.Bind.dtobase import DtoBase
from libs.Bind.observableCollection import ObservableCollection

class TblPlcCIOmemAbbr(declarative_base()):
    __tablename__ = 'TblPlcCIOmemAbbr'
    id = Column(Integer, primary_key=True)
    memIndex = Column(Integer)
    memAddr = Column(String)
    memname = Column(String)
    Bz = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblPlcCIOmemAbbr.HandlerBase(TblPlcCIOmemAbbr, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblPlcCIOmemAbbr.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
