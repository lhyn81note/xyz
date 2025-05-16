from models.__base__ import *
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

class TblSensorBaseValue(declarative_base()):
    __tablename__ = 'TblSensorBaseValue'
    SensorKind = Column(Integer, primary_key=True)
    ljABSensorDist = Column(Float)
    ljCDSensorDist = Column(Float)
    zjACSensorDist = Column(Float)
    zjBDSensorDist = Column(Float)
    ljASensorDist = Column(Float)
    ljBSensorDist = Column(Float)
    ljCSensorDist = Column(Float)
    ljDSensorDist = Column(Float)
    zjASensorDist = Column(Float)
    zjBSensorDist = Column(Float)
    zjCSensorDist = Column(Float)
    zjDSensorDist = Column(Float)
    zjASensorDir = Column(Float)
    zjBSensorDir = Column(Float)
    zjCSensorDir = Column(Float)
    zjDSensorDir = Column(Float)
    ljAzxzxDist = Column(Float)
    ljBzxzxDist = Column(Float)
    ljCzxzxDist = Column(Float)
    ljDzxzxDist = Column(Float)
    zjAhxzxDist = Column(Float)
    zjBhxzxDist = Column(Float)
    zjChxzxDist = Column(Float)
    zjDhxzxDist = Column(Float)
    GrossWeightA = Column(Float)
    GrossWeightB = Column(Float)
    GrossWeightC = Column(Float)
    GrossWeightD = Column(Float)
    Jzt1Weight = Column(Float)
    Jzt2Weight = Column(Float)
    BdgJzt1hxwy = Column(Float)
    BdgJzt2hxwy = Column(Float)
    BdgJzt12hxjl = Column(Float)
    BdlJzt1hxwy = Column(Float)
    BdlJzt2hxwy = Column(Float)
    BdlJzt12hxjl = Column(Float)
    Jzt1cxwy = Column(Float)
    Jzt2cxwy = Column(Float)
    HtabJzmZxkjl = Column(Float)
    HtcdJzmZxkjl = Column(Float)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblSensorBaseValue.HandlerBase(TblSensorBaseValue, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblSensorBaseValue.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
