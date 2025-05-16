from models.__base__ import *
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

class TblBogieTryParamSet(declarative_base()):
    __tablename__ = 'TblBogieTryParamSet'
    id = Column(Integer, primary_key=True)
    zxjxh = Column(String)
    paramNo = Column(String)
    paramName = Column(String)
    stdValue = Column(Float)
    diffLow = Column(Float)
    diffUp = Column(Float)
    valueunit = Column(String)
    Bz = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblBogieTryParamSet.HandlerBase(TblBogieTryParamSet, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblBogieTryParamSet.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
