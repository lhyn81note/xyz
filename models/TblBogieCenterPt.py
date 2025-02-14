from models.__base__ import *
from libs.Bind.dtobase import DtoBase
from libs.Bind.observableCollection import ObservableCollection

class TblBogieCenterPt(declarative_base()):
    __tablename__ = 'TblBogieCenterPt'
    zxjxh = Column(String, primary_key=True)
    zxjzs = Column(Integer)
    zxAB = Column(Float)
    zxCD = Column(Float)
    Jzt12ZxDist = Column(Float)
    zjASensorDist = Column(Float)
    zjBSensorDist = Column(Float)
    zjCSensorDist = Column(Float)
    zjDSensorDist = Column(Float)
    Jzt1HxSensorDist = Column(Float)
    Jzt2HxSensorDist = Column(Float)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblBogieCenterPt.HandlerBase(TblBogieCenterPt, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblBogieCenterPt.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
