import json
from pydantic import BaseModel, Field
from typing import List
import snap7
from snap7.util import set_bool

# 定义 Pydantic 模型
class Pt(BaseModel):
    id: str = Field(..., description="命令的唯一标识")
    name: str = Field(..., description="命令的名称")
    cmdtype: str = Field(..., alias="cmdtype", description="命令类型")
    addr: str = Field(..., description="地址")
    vartype: str = Field(..., description="变量类型")
    monitor: List[str] = Field(..., description="监控信号列表")

class Plc:

    def __init__(self, config_file: str, addr: str, protocal: str = "modbus", interval: int = 1000):

        self.filepath = config_file
        self.addr = addr
        self.protocal = protocal
        self.interval = interval  # 默认间隔时间
        self.client = None
        self.alive = False  # PLC是否在线
        self.pts = None

    def load_config(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.pts = [Pt(**value) for value in data.values()]

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

    def exe(self, cmd_id):
        if self.protocal == "modbus":
            pass
        elif self.protocal == "s7":
            # try:
                for pt in self.pts:
                    if (pt.id == cmd_id) and (pt.cmdtype == "cmd") and (pt.vartype == "BOOL"):
                        addrs = pt.addr.split(",")
                        db = int(addrs[0].split(":")[1])  # Extract DB number
                        start = int(addrs[1].split(":")[1])  # Extract start address
                        offset = int(addrs[2].split(":")[1])

                        data = bytearray(1)
                        # 使用set_bool方法将指定位置设置为True
                        set_bool(data, 0, offset, True)
                        # 写入数据到PLC的指定DB块和地址
                        self.client.db_write(db, start, data)
                        print(f"Set {pt.name} at {pt.addr} to True.")
                        break
                    else:
                        print(f"指令不匹配!{cmd_id}")
            # except Exception as e:
            #     print(f"Error executing command {cmd_id}: {e}")

if __name__ == "__main__":
    plc = Plc(config_file="plc.json", addr="172.16.1.95:0:2", protocal="s7", interval=1000)
    plc.load_config()
    for pt in plc.pts:
        print(pt)
        print("-" * 40)
    plc.connect()
    print(f"PLC is alive: {plc.alive}")
    plc.exe("cmd1")