from abc import abstractmethod, ABCMeta
from typing import List, Dict, TypeVar, Union
from enum import Enum

__all__ = ["plc"]

T=TypeVar("T")

class MODBUS_AREA(Enum):
    Coil=0
    InCoil=1
    Reg=2
    InReg=3

class IO(Enum):
    IN=0
    OUT=1

class MODBUS_VARTYPE(Enum):
    Bool=0
    Int_16=1
    Int_32=2
    Real_32=4
    
class BYTE_ENDIAN(Enum):
    BIG=0
    LITTLE=1

class WORD_ENDIAN(Enum):
    BIG=0
    LITTLE=1

class BasePlc(metaclass = ABCMeta):
    def __init__(self):
           self._isalive=False
           pass

    @abstractmethod
    def conn(self)->bool:
        pass

    @abstractmethod
    def disconn(self)->bool:
        pass

    def isalive(self)->bool:
        return self._isalive

    @abstractmethod
    def read_coils(self, area:MODBUS_AREA, start_address:int, count:int) -> Union[List[bool] , None] :
        pass

    @abstractmethod
    def write_coil(self, area:MODBUS_AREA, start_address:int, count:int, values:List[bool]) -> bool:
        pass

    @abstractmethod
    def read_regs(self, area:MODBUS_AREA, start_address:int, count:int) -> Union[List[T] , None] :
        pass

    @abstractmethod
    def write_reg(self, area:MODBUS_AREA, start_address:int, count:int, values:List[T]) -> bool:
        pass