from models.__base__ import *
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

class TblSensorData(declarative_base()):
    __tablename__ = 'TblSensorData'
    id = Column(Integer, primary_key=True)
    Zxjxh = Column(String)
    datakind = Column(Integer)
    dataIndex = Column(Integer)
    dataValue = Column(Float)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblSensorData.HandlerBase(TblSensorData, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblSensorData.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
