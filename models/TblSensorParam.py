from models.__base__ import *
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

class TblSensorParam(declarative_base()):
    __tablename__ = 'TblSensorParam'
    SensorNo = Column(Integer, primary_key=True)
    DataIndexPc = Column(Integer)
    DataIndexPlc = Column(Integer)
    SensorName = Column(String)
    PlcMinAD = Column(Float)
    PlcMaxAD = Column(Float)
    PhyMinData = Column(Float)
    PhyMaxData = Column(Float)
    multiK = Column(Float)
    modifyoffset = Column(Float)
    DataUnit = Column(String)
    SensorKind = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblSensorParam.HandlerBase(TblSensorParam, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblSensorParam.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
