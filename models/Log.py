from models.__base__ import *
from libs.Bind.dtobase import DtoBase
from libs.Bind.observableCollection import ObservableCollection

class Log(declarative_base()):
    __tablename__ = 'Log'
    Id = Column(String, primary_key=True)
    Content = Column(String)
    LogType = Column(String)
    LogTime = Column(DateTime)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = Log.HandlerBase(Log, engine)

    def dto(self):
        dto = DtoBase()
        for propname in Log.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
