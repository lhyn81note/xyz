from models.__base__ import *
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

class TblResultMx(declarative_base()):
    __tablename__ = 'TblResultMx'
    id = Column(String, primary_key=True)
    syjgbh = Column(String)
    PosiNo = Column(Integer)
    PosiName = Column(String)
    StdValue = Column(String)
    MeaValue = Column(String)
    StdValueMin = Column(String)
    StdValueMax = Column(String)
    Result = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblResultMx.HandlerBase(TblResultMx, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblResultMx.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
