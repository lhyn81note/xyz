from models.__base__ import *
from libs.binding.dtobase import DtoBase
from libs.binding.observableCollection import ObservableCollection

class FaultCode():

    class Entity(declarative_base()):
        __tablename__ = 'FaultCode'
        Code = Column(String, primary_key=True)
        Level = Column(String)
        Description = Column(String)
        Source = Column(String)
        IsUse = Column(String)
        Remark = Column(String)

    class HandlerBase(ServiceBase):
        def __init__(self, T, engine):
            super().__init__(T, engine)

    def __init__(self, engine) -> None:
        self.Handler = FaultCode.HandlerBase(FaultCode.Entity, engine)

    def toDto(self, entity):
        dto = DtoBase()
        for propname in FaultCode.Entity.__table__.columns.keys():
            dto.__setattr__(propname, getattr(entity, propname))
        return dto
    
    def fromDto(self, dto):
        entity = FaultCode.Entity()
        for propname in FaultCode.Entity.__table__.columns.keys():
            entity.__setattr__(propname, getattr(dto, propname))
        return entity
