from abc import abstractmethod, ABCMeta
from typing import List, Dict, TypeVar, Union
import threading
import time
from . import BasePlc
from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.constants import Endian
from enum import Enum

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

class ModbusTcp(BasePlc):

    def __init__(self):
        super().__init__()
        self.client=None
        self.config=None
        self.running=False
        self.callbacks = []

    def register_callback(self, callback):
        if callable(callback):
            self.callbacks.append(callback)
        else:
            raise ValueError("无法调用对象")

    def trigger_callbacks(self, *args, **kwargs):
        for callback in self.callbacks:
            if callback is not None:
                callback(*args, **kwargs)

    def init(self, config=None, host=None, port=502, timeout=1000) -> bool:
        if config:
            self.config = config
            self.client = ModbusTcpClient(self.config['host'], self.config['port'], timeout=self.config['timeout'])
        else:
            if host:
                self.client = ModbusTcpClient(host, port=port, timeout=timeout)
            else:
                raise "未指定PLC地址!"

    def __str__(self)->str:
        if self.config:
            return f"{self.config['host']}::{self.config['port']}::{len(self.config['pts'])}"
        else:
            return f"无配置文件"
            
    def conn(self)->bool: 
        self.client.connect()
        return self.client.connected
    
    def disconn(self)->bool:
        try:
            self.client.close()
            return True
        except Exception as e:
            #log
            return False
        
    def isalive(self) -> bool:
        return self.client.connected

    def read_coils(self, area:MODBUS_AREA, start_address:int, count:int, slave:int=1) -> Union[List[bool] , None] :
        ret=None
        if area==MODBUS_AREA.Coil:
            ret = self.client.read_coils(start_address,count,slave=slave)
        elif area==MODBUS_AREA.InCoil:
            ret = self.client.read_discrete_inputs(start_address,count,slave=slave)
        else:
            #log
            raise f"错误区:{area}!"
        if ret.isError():
            #log
            return False
        else:
            return ret.bits
        
    def write_coil(self, address:int, value:bool, slave:int=1) -> bool:
        ret = self.client.write_coil(address,value,slave=slave)        
        if ret.isError():
            #log
            return False
        else:
            return True
        
    def read_regs(self, area:MODBUS_AREA, start_address:int, count:int, slave:int=1) -> Union[List[int] , None] :
        ret=None
        if area==MODBUS_AREA.Reg:
            ret = self.client.read_holding_registers(start_address,count,slave=slave)
        elif area==MODBUS_AREA.InReg:
            ret = self.client.read_input_registers(start_address,count,slave=slave)
        else:
            #log
            raise f"错误区:{area}!"
        if ret.isError():
            #log
            return False
        else:
            return ret     
           
    def write_reg(self, address:int,  value:int, slave:int=1) -> bool:
        ret = self.client.write_register(address,value,slave=slave)        
        if ret.isError():
            #log
            return False
        else:
            return True
        
    def read_pt(self, pt, byte_order=Endian.BIG, word_order=Endian.BIG):

        # if pt['io']==IO.OUT:
        #     return
        
        ret=None

        if pt['type']==MODBUS_VARTYPE.Bool:
            addrs = [int(x) for x in pt['address'].split('.')]
            if pt['area']==MODBUS_AREA.Coil:
                ret = self.client.read_coils(addrs[0]*8+addrs[1], 1, pt['slave']).bits
                # print(f"{pt['address']}-->{ret}")
                ret = ret[0]
            elif pt['area']==MODBUS_AREA.InCoil:
                ret = self.client.read_discrete_inputs(addrs[0]*8+addrs[1], 1, pt['slave']).bits
                # print(f"{pt['address']}-->{ret}")
                ret = ret[0]
            elif pt['area']==MODBUS_AREA.Reg:
                ret = self.client.read_holding_registers(int(addrs[0]), 1, slave=pt['slave'])
                decoder = BinaryPayloadDecoder.fromRegisters(ret.registers, byteorder=byte_order, wordorder=word_order)
                ret = decoder.decode_bits(package_len=1)  
                # print(f"--->{ret}")
                ret = ret[addrs[1]]    
            else:
                raise "错误点位"
        else:
            bytes = -1
            if pt['type']==MODBUS_VARTYPE.Int_16: bytes=1
            elif pt['type']==MODBUS_VARTYPE.Int_32: bytes=2
            elif pt['type']==MODBUS_VARTYPE.Real_32: bytes=2            
            ret = self.client.read_holding_registers(int(pt['address']), bytes, pt['slave'])
            decoder = BinaryPayloadDecoder.fromRegisters(ret.registers, Endian.BIG, Endian.BIG)
            if pt['type']==MODBUS_VARTYPE.Int_16: ret=decoder.decode_16bit_int()
            elif pt['type']==MODBUS_VARTYPE.Int_32: ret=decoder.decode_32bit_int()
            elif pt['type']==MODBUS_VARTYPE.Real_32: ret=decoder.decode_32bit_float()      
        pt['value']=ret

    def write_pt(self, pt, val):

        if pt['io']==IO.IN:
            return

        if pt['type']==MODBUS_VARTYPE.Bool:
            addrs = [int(x) for x in pt['address'].split('.')]
            if pt['area']==MODBUS_AREA.Coil:
                ret = self.client.write_coil(addrs[0]*8+addrs[1], val, pt['slave'])
            elif pt['area']==MODBUS_AREA.Reg:
                pass   
            else:
                raise "错误点位"
        else:
            builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.BIG)
            if pt['type']==MODBUS_VARTYPE.Int_16: builder.add_16bit_int(val)
            elif pt['type']==MODBUS_VARTYPE.Int_32: builder.add_32bit_int(val)
            elif pt['type']==MODBUS_VARTYPE.Real_32: builder.add_32bit_float(val)    
            payload = builder.to_registers()
            self.client.write_registers(int(pt['address']), payload)

    def read_all(self):
        print("开始读取?")
        while self.running:
            for i in range(len(self.config['pts'])):
                pt=self.config['pts'][i]
                # if pt['io']==IO.OUT: continue
                self.read_pt(pt)
                self.trigger_callbacks((i,pt['value']))
                # print(pt_obj['value'])
            time.sleep(self.config['interval'])
        
        # # get max address
        # ADDRS = [pt['address'].split('.')[1] for pt in self.config['pts'].values() if pt['io']==IO.IN]
        # MAX_ADDR = max(ADDRS)
        # MIN_ADDR = min(ADDRS)
        # COUNT = MAX_ADDR-MIN_ADDR+1

        # # read all bytes
        # all_coils = self.client.read_holding_registers(address=MIN_ADDR, count=COUNT)
        # decoder = BinaryPayloadDecoder.fromRegisters(all_coils.registers)
        # decoder.decode_bits(COUNT)

    def loop(self):
        thread = threading.Thread(target=self.read_all)
        thread.daemon = True 
        thread.start()

    def stop(self):
        self.running = False

    def start(self):
        self.running = True