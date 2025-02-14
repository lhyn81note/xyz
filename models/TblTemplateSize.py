from models.__base__ import *
from libs.Bind.dtobase import DtoBase
from libs.Bind.observableCollection import ObservableCollection

class TblTemplateSize(declarative_base()):
    __tablename__ = 'TblTemplateSize'
    ybbh = Column(String, primary_key=True)
    Bdlzxkjl = Column(Float)
    Bdlzxjl1 = Column(Float)
    Bdlzxjl2 = Column(Float)
    Bdlzxjgmjl1 = Column(Float)
    Bdlzxjgmjl2 = Column(Float)
    Bdgdmjl = Column(Float)
    bdlzxHt13hxpc = Column(Float)
    bdlzxHt24hxpc = Column(Float)
    Ht1JzzxkSkdmjl = Column(Float)
    Ht2JzzxkSkdmjl = Column(Float)
    Ht3JzzxkSkdmjl = Column(Float)
    Ht4JzzxkSkdmjl = Column(Float)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblTemplateSize.HandlerBase(TblTemplateSize, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblTemplateSize.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
