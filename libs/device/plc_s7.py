import json,time
import logging
from pydantic import BaseModel, Field
from typing import List
import snap7
from snap7.util import set_bool, get_bool, set_int, get_int, set_real, get_real, set_word, get_word
from typing import Union
import threading
from . import BasePlc
from ..notify import MsgType, MsgBroker

class Pt(BaseModel):
    id: str = Field(..., description="命令的唯一标识") # 默认值为Field表示映射到json的key
    name: str = Field(..., description="命令的名称")
    addr: str = Field(..., description="地址")
    iotype: str = Field(..., description="读写类型")
    vartype: str = Field(..., description="变量类型")
    done: List[str] = Field(..., description="监控信号列表")
    range: Union[List[int], None] = Field(..., description="数值范围")
    value: Union[bool, int, float]= None  # 默认值不是Field表示不映射, 可以规定类型

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

class S7(BasePlc):

    def __init__(self, config_file: str, addr: str, interval: int, msgbroker: MsgBroker):
        super().__init__()
        self.filepath = config_file
        self.addr = addr
        self.protocal = "s7"
        self.interval = interval  # 默认间隔时间
        self.msgbroker = msgbroker # 用于发布消息
        # self.client_r = None
        # self.client_w = None
        # self.pts = {}
        # self.callbacks = []  # 用于存储回调函数

    def load_config(self) -> bool:
        # try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                ptlist = [Pt(**value) for value in data.values()]
                for pt in ptlist:
                    self.pts[pt.id] = pt
            return True
        # except Exception as e:
            logging.error(f"加载配置文件失败: {self.filepath}")
            return False

    def connect(self) -> bool:
        try:
            self.client_r = snap7.client.Client()
            self.client_w = snap7.client.Client()
            ip = self.addr.split(":")[0]
            rack = int(self.addr.split(":")[1]) if ":" in self.addr else 0
            slot = int(self.addr.split(":")[2]) if ":" in self.addr else 1

            self.client_r.connect(ip, rack, slot)  # Rack=0, Slot=1 are typical defaults 
            self.client_w.connect(ip, rack, slot)  # Rack=0, Slot=1 are typical defaults

            if self.alive:
                logging.info("S7连接成功.")
                return True
            else:
                logging.error("S7链接失败")
                return False

        except Exception as e:
            logging.error(f"S7连接出错: {e}")
            return False

    def write(self, ptId, value) -> bool:

        pt = self.pts.get(ptId)

        if pt is None:
            logging.error(f"指令不存在!{ptId}")
            return False

        if (self.client_w is None) or self.alive==False:
            logging.error(f"PLC未连接!")
            return False

        if pt.iotype == "i":
            logging.error(f"输入指令不能写入!{pt.iotype}")
            return False

        addrs = pt.addr.split(",")
        db = int(addrs[0].split(":")[1])  
        start_byte = int(addrs[1].split(":")[1])  

        try:
            if (pt.vartype == "BOOL"):
                offset = int(addrs[2].split(":")[1])
                data = bytearray(1) 
                set_bool(data, 0, offset, value==True)# 使用set_bool方法将指定位置设置为True
                self.client_w.db_write(db, start_byte, data)# 写入数据到PLC的指定DB块和地址
                return True

            elif (pt.vartype == "INT"):
                data = bytearray(2)  
                set_int(data, 0, value)  
                self.client_w.db_write(db, start_byte, data)  
                return True

            elif (pt.vartype == "WORD"):
                data = bytearray(2) 
                set_word(data, 0, value)  
                self.client_w.db_write(db, start_byte, data)  
                return True

            elif (pt.vartype == "REAL"):
                data = bytearray(4)  
                set_real(data, 0, value)  
                self.client_w.db_write(db, start_byte, data)  
                return True

            else:
                logging.error(f"点类型错误:{pt.vartype}")
                return False

        except Exception as e:
            logging.error(f"写入PLC错误:{e}")
            return False

    def read(self, ptId)->[bool |int | float]:

        pt = self.pts.get(ptId)

        if pt is None:
            logging.error(f"PLC指令不存在!{ptId}")
            return False

        if (self.client_r is None) or self.alive==False:
            logging.error(f"PLC未连接,无法读取")
            return False

        addrs = pt.addr.split(",")
        db = int(addrs[0].split(":")[1])  
        start_byte = int(addrs[1].split(":")[1])  

        try:

            if (pt.vartype == "BOOL"):
                offset = int(addrs[2].split(":")[1])
                data = self.client_r.db_read(db, start_byte, 1) # 读取1个字节
                return get_bool(data, 0, offset)

            elif (pt.vartype == "INT"):
                data = self.client_r.db_read(db, start_byte, 2) # 读取2个字节
                return get_int(data, 0)

            elif (pt.vartype == "WORD"):
                data = self.client_r.db_read(db, start_byte, 2) # 读取2个字节
                return get_word(data, 0)

            elif (pt.vartype == "REAL"):
                data = self.client_r.db_read(db, start_byte, 4) # 读取4个字节
                return get_real(data, 0)

            else:
                logging.error(f"点类型错误!{pt.vartype}")
                return None
                
        except Exception as e:
            logging.error(f"读取PLC错误:{e}")
            return None

    def scan(self):

        def readall():
            while True:
                # 先发一次连接状态
                self.msgbroker.publish(MsgType.alarm, {
                    'source': "PLC",
                    'subject':'connect',
                    'content': self.alive,
                })

                if self.alive==False: # 如果断开则连接
                    self.connect()
    
                else: # 如果连着则读取
                    for pt in self.pts.values():
                        pt.value = self.read(pt.id)

                        if pt.value is None:
                            self.msgbroker.publish(MsgType.alarm, {
                                'source': "PLC",
                                'subject':'alarm',
                                'content': "PLC读点失败",
                            })
                        else:
                            if not pt.isValid:
                                self.msgbroker.publish(MsgType.alarm, {
                                    'source': "PLC",
                                    'subject':'alarm',
                                    'content': pt.name,
                                })

                time.sleep(self.interval / 1000)
                self.trigger_callbacks()

        thread = threading.Thread(target=readall, daemon=True)
        thread.start()


if __name__ == "__main__":
    plc = Plc(config_file="plc.json", addr="172.16.1.95:0:2", protocal="s7", interval=500)
    plc.load_config()
    plc.connect()
    plc.write("data1",100)
    plc.write("data2",65523)
    plc.write("data3",11.22)
    plc.scan()