from models.__base__ import *
from libs.Bind.dtobase import DtoBase
from libs.Bind.observableCollection import ObservableCollection

class TblUser(declarative_base()):
    __tablename__ = 'TblUser'
    id = Column(String, primary_key=True)
    UserName = Column(String)
    LoginPassword = Column(String)
    UserClass = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = TblUser.HandlerBase(TblUser, engine)

    def dto(self):
        dto = DtoBase()
        for propname in TblUser.__table__.columns.keys():
            dto.__setattr__(propname, getattr(self, propname))
        return dto
