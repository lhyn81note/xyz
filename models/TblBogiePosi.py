from models.__base__ import *
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

class TblBogiePosi(declarative_base()):
    __tablename__ = 'TblBogiePosi'
    id = Column(String, primary_key=True)
    zxjxh = Column(String)
    sybwbh = Column(Integer)
    sybwmc = Column(String)
    stdValue = Column(Float)
    diffLow = Column(Float)
    diffUp = Column(Float)
    valueunit = Column(String)
    sybwAbbr = Column(String)
    Isprint = Column(String)
    dataKind = Column(String)
    dataXh = Column(Float)
    memBz = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblBogiePosi.HandlerBase(TblBogiePosi, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblBogiePosi.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
