import json, time
import logging
from pydantic import BaseModel, Field
from typing import List, Union
import threading
from pymodbus.client import ModbusTcpClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from . import BasePlc
from ..notify import MsgType, MsgBroker

# Constants for Modbus configuration
# class MODBUS_AREA:
#     Coil = "Coil"       # Coil (output) - 0xxxx
#     InCoil = "InCoil"   # Discrete Input - 1xxxx
#     InReg = "InReg"     # Input Register - 3xxxx
#     Reg = "Reg"         # Holding Register - 4xxxx

# class MODBUS_VARTYPE:
#     Bool = "Bool"       # Boolean
#     Int_16 = "Int_16"   # 16-bit integer
#     Int_32 = "Int_32"   # 32-bit integer
#     Real_32 = "Real_32" # 32-bit float
#     Word = "Word"       # 16-bit unsigned integer

# class BYTE_ENDIAN:
#     BIG = Endian.BIG
#     LITTLE = Endian.LITTLE

# class WORD_ENDIAN:
#     BIG = Endian.BIG
#     LITTLE = Endian.LITTLE

# class IO:
#     IN = "i"
#     OUT = "o"

class Pt(BaseModel):
    id: str = Field(..., description="命令的唯一标识")
    name: str = Field(..., description="命令的名称")
    addr: str = Field(..., description="地址")
    iotype: str = Field(..., description="读写类型")
    vartype: str = Field(..., description="变量类型")
    done: List[str] = Field(..., description="监控信号列表")
    range: Union[List[int], None] = Field(..., description="数值范围")
    value: Union[bool, int, float] = None

    @property
    def isValid(self):
        if self.value is not None:
            if self.range is not None:
                check = self.range[0] <= self.value <= self.range[1]
                return check

            if self.vartype == "BOOL" and self.id.startswith("alarm"):
                check = self.value == False
                return check
            else:
                return True
        else:
            return False

class ModbusTcp(BasePlc):
    def __init__(self, config_file: str, addr: str, interval: int, msgbroker: MsgBroker):
        super().__init__()
        self.filepath = config_file
        self.addr = addr
        self.protocal = "modbus"
        self.interval = interval  # 默认间隔时间，单位毫秒
        self.msgbroker = msgbroker  # 用于发布消息
        self.byte_order = Endian.BIG
        self.word_order = Endian.LITTLE
        # self.client_r = None
        # self.client_w = None
        # self.pts = {}
        # self.callbacks = []  # 用于存储回调函数

    def load_config(self) -> bool:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                ptlist = [Pt(**value) for value in data.values()]
                for pt in ptlist:
                    self.pts[pt.id] = pt
            return True
        except Exception as e:
            logging.error(f"加载配置文件失败: {self.filepath}, 错误: {e}")
            return False

    def connect(self) -> bool:
        try:
            # Parse address (format: "ip:port")
            ip = self.addr.split(":")[0]
            port = int(self.addr.split(":")[1]) if ":" in self.addr else 502

            # Create ModbusTcpClient instances for reading and writing
            self.client_r = ModbusTcpClient(host=ip, port=port)
            self.client_w = ModbusTcpClient(host=ip, port=port)

            # Connect to the Modbus server
            self.client_r.connect()
            self.client_w.connect()

            if self.alive:
                logging.info("Modbus TCP连接成功.")
                return True
            else:
                logging.error("Modbus TCP连接失败")
                return False

        except Exception as e:
            logging.error(f"Modbus TCP连接出错: {e}")
            return False

    @property
    def alive(self) -> bool:
        try:
            return self.client_r.is_socket_open() and self.client_w.is_socket_open()
        except Exception as e:
            return False

    def write(self, ptId, value) -> bool:
        pt = self.pts.get(ptId)

        if pt is None:
            logging.error(f"指令不存在!{ptId}")
            return False

        if (self.client_w is None) or self.alive == False:
            logging.error(f"PLC未连接!")
            return False

        if pt.iotype == "i":
            logging.error(f"输入指令不能写入!{pt.iotype}")
            return False

        try:
            # Parse address
            addrs = pt.addr.split(",")
            address_parts = addrs[0].split(":")

            # Get the register/coil address
            if len(address_parts) > 1:
                address = int(address_parts[1])
            else:
                address = int(address_parts[0])

            # Handle different variable types
            if pt.vartype == "BOOL":
                # For boolean values, write to coil
                result = self.client_w.write_coil(address, value == True)
                return not result.isError()

            elif pt.vartype == "INT":
                # For 16-bit integers
                builder = BinaryPayloadBuilder(byteorder=self.byte_order, wordorder=self.word_order)
                builder.add_16bit_int(value)
                registers = builder.to_registers()
                result = self.client_w.write_registers(address, registers)
                return not result.isError()

            elif pt.vartype == "WORD":
                # For 16-bit unsigned integers
                builder = BinaryPayloadBuilder(byteorder=self.byte_order, wordorder=self.word_order)
                builder.add_16bit_uint(value)
                registers = builder.to_registers()
                result = self.client_w.write_registers(address, registers)
                return not result.isError()

            elif pt.vartype == "REAL":
                # For 32-bit floating point values
                builder = BinaryPayloadBuilder(byteorder=self.byte_order, wordorder=self.word_order)
                builder.add_32bit_float(value)
                registers = builder.to_registers()
                result = self.client_w.write_registers(address, registers)
                return not result.isError()

            else:
                logging.error(f"点类型错误:{pt.vartype}")
                return False

        except Exception as e:
            logging.error(f"写入PLC错误:{e}")
            return False

    def read(self, ptId) -> Union[bool, int, float, None]:
        pt = self.pts.get(ptId)

        if pt is None:
            logging.error(f"PLC指令不存在!{ptId}")
            return False

        if (self.client_r is None) or self.alive == False:
            logging.error(f"PLC未连接,无法读取")
            return False

        # try:
        # Parse address
        addrs = pt.addr.split(",")
        address_parts = addrs[0].split(":")

        # Get the register/coil address
        if len(address_parts) > 1:
            address = int(address_parts[1])
        else:
            address = int(address_parts[0])

        # Handle different variable types
        if pt.vartype == "BOOL":
            # For boolean values, read from coil or discrete input
            if pt.iotype == "i":
                result = self.client_r.read_discrete_inputs(address, 1)
            else:
                result = self.client_r.read_coils(address, 1)

            if result.isError():
                return None
            return result.bits[0]

        elif pt.vartype == "INT":
            # For 16-bit integers
            result = self.client_r.read_holding_registers(address, 1)
            if result.isError():
                return None
            decoder = BinaryPayloadDecoder.fromRegisters(
                result.registers, byteorder=self.byte_order, wordorder=self.word_order
            )
            return decoder.decode_16bit_int()

        elif pt.vartype == "WORD":
            # For 16-bit unsigned integers
            result = self.client_r.read_holding_registers(address, 1)
            if result.isError():
                return None
            decoder = BinaryPayloadDecoder.fromRegisters(
                result.registers, byteorder=self.byte_order, wordorder=self.word_order
            )
            return decoder.decode_16bit_uint()

        elif pt.vartype == "REAL":
            # For 32-bit floating point values
            result = self.client_r.read_holding_registers(address, 2)
            if result.isError():
                return None
            decoder = BinaryPayloadDecoder.fromRegisters(
                result.registers, byteorder=self.byte_order, wordorder=self.word_order
            )
            return decoder.decode_32bit_float()

        else:
            logging.error(f"点类型错误!{pt.vartype}")
            return None

        # except Exception as e:
        #     logging.error(f"读取PLC错误:{e}")
        #     return None

    def scan(self):
        def readall():
            while True:
                # 先发一次连接状态
                self.msgbroker.publish(MsgType.alarm, {
                    'source': "PLC",
                    'subject': 'connect',
                    'content': self.alive,
                })

                if self.alive == False:  # 如果断开则连接
                    self.connect()
                else:  # 如果连着则读取
                    for pt in self.pts.values():
                        pt.value = self.read(pt.id)

                        if pt.value is None:
                            logging.error(f"PLC读取错误:{pt.id}")
                        else:
                            if not pt.isValid:
                                self.msgbroker.publish(MsgType.alarm, {
                                    'source': "PLC",
                                    'subject': 'alarm',
                                    'content': pt.name,
                                })

                time.sleep(self.interval / 1000)
                self.trigger_callbacks()

        thread = threading.Thread(target=readall, daemon=True)
        thread.start()


if __name__ == "__main__":
    # Example usage
    plc = ModbusTcp(config_file="plc_modbus.json", addr="127.0.0.1:502", interval=500, msgbroker=None)
    plc.load_config()
    plc.connect()
    plc.write("data1", 100)
    plc.write("data2", 65523)
    plc.write("data3", 11.22)
    plc.scan()
