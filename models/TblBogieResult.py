from models.__base__ import *
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

class TblBogieResult(declarative_base()):
    __tablename__ = 'TblBogieResult'
    syjlbh = Column(String, primary_key=True)
    syrq = Column(DateTime)
    jcch = Column(String)
    jccx = Column(String)
    zxjbh = Column(String)
    zxjxh = Column(String)
    jxlx = Column(String)
    zxjzzrq = Column(DateTime)
    ldbh1 = Column(String)
    Ldxh1 = Column(String)
    ldbh2 = Column(String)
    Ldxh2 = Column(String)
    syczz = Column(String)
    syzt = Column(Integer)
    sygz = Column(String)
    syzjy = Column(String)
    syysy = Column(String)
    Kzjzl1 = Column(Float)
    Kzjzl2 = Column(Float)
    Mzjzl1 = Column(Float)
    Mzjzl2 = Column(Float)
    FreeLoadf1 = Column(Float)
    FreeLoadf2 = Column(Float)
    NoFreeLoadf1 = Column(Float)
    NoFreeLoadf2 = Column(Float)
    BzInfo = Column(String)
    QrCode = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblBogieResult.HandlerBase(TblBogieResult, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblBogieResult.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
