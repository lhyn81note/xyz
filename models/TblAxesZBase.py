from models.__base__ import *
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

class TblAxesZBase(declarative_base()):
    __tablename__ = 'TblAxesZBase'
    Cztbh = Column(String, primary_key=True)
    Tlbj = Column(Float)
    Tljl = Column(Float)
    H1 = Column(Float)
    H2 = Column(Float)
    H3 = Column(Float)
    H4 = Column(Float)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblAxesZBase.HandlerBase(TblAxesZBase, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblAxesZBase.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
