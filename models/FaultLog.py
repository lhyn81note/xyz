from models.__base__ import *
from libs.Bind.dtobase import DtoBase
from libs.Bind.observableCollection import ObservableCollection

class FaultLog(declarative_base()):
    __tablename__ = 'FaultLog'
    Id = Column(String, primary_key=True)
    OccurTime = Column(DateTime)
    LastTime = Column(DateTime)
    ConfirTime = Column(DateTime)
    Code = Column(String)
    Level = Column(String)
    Description = Column(String)
    Source = Column(String)
    Attach = Column(String)
    Status = Column(String)
    Remark = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = FaultLog.HandlerBase(FaultLog, engine)

    def dto(self):
        dto = DtoBase()
        for propname in FaultLog.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
