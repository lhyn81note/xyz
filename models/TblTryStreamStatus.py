from models.__base__ import *
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

class TblTryStreamStatus(declarative_base()):
    __tablename__ = 'TblTryStreamStatus'
    Ztbj = Column(String, primary_key=True)
    Ztmc = Column(String)
    plcSdBitAddr = Column(String)
    plcWordAddr = Column(String)
    plcRvBitAddr = Column(String)
    Wcsj = Column(Integer)
    Sm = Column(String)
    rggy = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblTryStreamStatus.HandlerBase(TblTryStreamStatus, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblTryStreamStatus.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
