from models.__base__ import *
from libs.Bind.dtobase import DtoBase
from libs.Bind.observableCollection import ObservableCollection

class TblNowSheet(declarative_base()):
    __tablename__ = 'TblNowSheet'
    syjlbh = Column(String, primary_key=True)
    zxjxh = Column(String)
    syrq = Column(DateTime)
    syzt = Column(Integer)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblNowSheet.HandlerBase(TblNowSheet, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblNowSheet.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
