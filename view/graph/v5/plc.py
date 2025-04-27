import json
from pydantic import BaseModel, Field
from typing import List

# 定义 Pydantic 模型
class Pt(BaseModel):
    id: str = Field(..., description="命令的唯一标识")
    name: str = Field(..., description="命令的名称")
    cmdtype: str = Field(..., alias="cmdtype", description="命令类型")
    addr: str = Field(..., description="地址")
    vartype: str = Field(..., description="变量类型")
    monitor: List[str] = Field(..., description="监控信号列表")

class Plc:

    def __init__(self):
        self.pts = None

    def load_config(self, config_file: str):
        with open(config_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.pts = [Pt(**value) for value in data.values()]

if __name__ == "__main__":
    plc = Plc()
    plc.load_config("plc.json")
    for pt in plc.pts:
        print(pt)
        print("-" * 40)