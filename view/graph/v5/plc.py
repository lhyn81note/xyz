import json,time
from pydantic import BaseModel, Field
from typing import List
import snap7
from snap7.util import set_bool, get_bool, set_int, get_int, set_real, get_real, set_word, get_word
from typing import Union
import threading

# 定义 Pydantic 模型
class Pt(BaseModel):
    id: str = Field(..., description="命令的唯一标识") # 默认值为Field表示映射到json的key
    name: str = Field(..., description="命令的名称")
    iotype: str = Field(..., description="读写类型")
    addr: str = Field(..., description="地址")
    vartype: str = Field(..., description="变量类型")
    monitor: List[str] = Field(..., description="监控信号列表")
    value: Union[bool, int, float]= None  # 默认值不是Field表示不映射, 可以规定类型

class Plc:

    def __init__(self, config_file: str, addr: str, protocal: str = "modbus", interval: int = 1000):

        self.filepath = config_file
        self.addr = addr
        self.protocal = protocal
        self.interval = interval  # 默认间隔时间
        self.client = None
        self.alive = False  # PLC是否在线
        self.pts = {}

    def load_config(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            ptlist = [Pt(**value) for value in data.values()]
            for pt in ptlist:
                self.pts[pt.id] = pt

    def connect(self):

        if self.protocal == "modbus":
            print(f"Connecting to PLC at {self.addr} using Modbus protocol...")
            # Add Modbus connection logic here
            self.alive = True  # Simulate successful connection

        elif self.protocal == "s7":
            print(f"Connecting to PLC at {self.addr} using Profinet S7 protocol...")
            try:
                self.client = snap7.client.Client()
                ip = self.addr.split(":")[0]
                rack = int(self.addr.split(":")[1]) if ":" in self.addr else 0
                slot = int(self.addr.split(":")[2]) if ":" in self.addr else 1
                self.client.connect(ip, rack, slot)  # Rack=0, Slot=1 are typical defaults
                self.alive = self.client.get_connected()
                if self.alive:
                    print("Connection successful.")
                else:
                    print("Failed to connect.")
            except Exception as e:
                print(f"Error connecting to PLC: {e}")
                self.alive = False

    def write(self, ptId, value) -> bool:

        pt = self.pts.get(ptId)

        if pt is None:
            print(f"指令不存在!{ptId}")
            return False

        if (self.client is None) or self.alive==False:
            print(f"PLC未连接!")
            return False

        if pt.iotype == "i":
            print(f"输入指令不能写入!{pt.iotype}")
            return False

        if self.protocal == "modbus":
            pass

        elif self.protocal == "s7":

            addrs = pt.addr.split(",")
            db = int(addrs[0].split(":")[1])  
            start_byte = int(addrs[1].split(":")[1])  

            if (pt.vartype == "BOOL"):
                offset = int(addrs[2].split(":")[1])
                data = bytearray(1) 
                set_bool(data, 0, offset, value==True)# 使用set_bool方法将指定位置设置为True
                self.client.db_write(db, start_byte, data)# 写入数据到PLC的指定DB块和地址
                print(f"布尔指令 {pt.name} 执行成功")
                return True

            elif (pt.vartype == "INT"):
                data = bytearray(2)  
                set_int(data, 0, value)  
                self.client.db_write(db, start_byte, data)  
                print(f"整形指令 {pt.name} 执行成功")
                return True

            elif (pt.vartype == "WORD"):
                data = bytearray(2) 
                set_word(data, 0, value)  
                self.client.db_write(db, start_byte, data)  
                print(f"字指令 {pt.name} 执行成功")
                return True

            elif (pt.vartype == "REAL"):
                data = bytearray(4)  
                set_real(data, 0, value)  
                self.client.db_write(db, start_byte, data)  
                print(f"实数指令 {pt.name} 执行成功")
                return True

            else:
                print(f"点类型错误:{pt.vartype}")
                return False

    def read(self, ptId)->[bool |int | float]:
        pt = self.pts.get(ptId)

        if pt is None:
            print(f"指令不存在!{ptId}")
            return False

        if (self.client is None) or self.alive==False:
            print(f"PLC未连接!")
            return False

        if self.protocal == "modbus":
            pass

        elif self.protocal == "s7":

            addrs = pt.addr.split(",")
            db = int(addrs[0].split(":")[1])  
            start_byte = int(addrs[1].split(":")[1])  

            if (pt.vartype == "BOOL"):
                offset = int(addrs[2].split(":")[1])
                data = self.client.db_read(db, start_byte, 1) # 读取1个字节
                return get_bool(data, 0, offset)

            elif (pt.vartype == "INT"):
                data = self.client.db_read(db, start_byte, 2) # 读取2个字节
                return get_int(data, 0)

            elif (pt.vartype == "WORD"):
                data = self.client.db_read(db, start_byte, 2) # 读取2个字节
                return get_word(data, 0)

            elif (pt.vartype == "REAL"):
                data = self.client.db_read(db, start_byte, 4) # 读取4个字节
                return get_real(data, 0)

            else:
                print(f"点类型错误!{pt.vartype}")
                return None

    def scan(self):
        def readall():
            while True:
                print("-" * 40)
                if self.protocal == "modbus":
                    pass
                elif self.protocal == "s7":
                    for pt in self.pts.values():
                        print(pt)
                        pt.value = self.read(pt.id)
                        print(f"ID: {pt.id}, Value: {pt.value}")
                time.sleep(self.interval / 1000)

        thread = threading.Thread(target=readall)
        thread.start()

if __name__ == "__main__":

    plc = Plc(config_file="plc.json", addr="172.16.1.95:0:2", protocal="s7", interval=3000)
    plc.load_config()

    plc.connect()
    print(f"PLC is alive: {plc.alive}")

    plc.write("data1",100)
    plc.write("data2",65523)
    plc.write("data3",11.22)


    # ret = plc.read("data1")
    # print(f"读取数据: {ret}")

    plc.scan()