from models.__base__ import *
from libs.Bind.dtobase import DtoBase
from libs.Bind.observableCollection import ObservableCollection

class TblBogieLoaderInfo(declarative_base()):
    __tablename__ = 'TblBogieLoaderInfo'
    id = Column(Integer, primary_key=True)
    CRHxh = Column(String)
    chNo0 = Column(Integer)
    chNo1 = Column(String)
    BogieNo = Column(Integer)
    Loadf1 = Column(Float)
    Loadf2 = Column(Float)
    LoadfDN = Column(Float)
    LoadfUp = Column(Float)
    FullLoadf1 = Column(Float)
    FullLoadf2 = Column(Float)
    FullLoadfDN = Column(Float)
    FullLoadfUp = Column(Float)
    FreeLoadf1 = Column(Float)
    FreeLoadf2 = Column(Float)
    NoFreeLoadf1 = Column(Float)
    NoFreeLoadf2 = Column(Float)
    Reserve1 = Column(String)
    Reserve2 = Column(String)
    Reserve3 = Column(String)
    Reserve4 = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblBogieLoaderInfo.HandlerBase(TblBogieLoaderInfo, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblBogieLoaderInfo.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
