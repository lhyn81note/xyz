import asyncio
from datetime import datetime
import json

class CmdMananger:

    def __init__(self):
        self.flow_file = None
        self.meta = {}
        self.flow = {}  # Placeholder for flow configuration
        self.head_node_id = None  # Placeholder for head node ID
        self.cmds = {}
        self.cmdObjs = {}
        self.nodes = {}
        self.flowStatus = 0  # 0: idle, 1: running, 2: paused, 3: stopped 4: error
        self.cursor = ""  # Placeholder for flow configuration

    '''
    流程配置文件操作
    '''
    def loadFlow(self, flow_file) -> bool:

        with open(flow_file, 'r', encoding='utf-8') as file:

            self.flow_file = flow_file
            json_str = file.read()
            data = json.loads(json_str)

            if self.validateFlow(data):
                self.meta = data.get("meta")
                self.flow = {k: v for k, v in data.get("flow").items() if k != "head_node_id"}
                self.head_node_id = data.get("flow").get("head_node_id")
                self.cmds = data.get("cmds")
                self.nodes = data.get("nodes")


    def saveFlow(self):
        with open(self.flow_file, 'w') as file:
            data = {
                "meta": self.meta,
                "flow": self.flow,
                "cmds": self.cmds,
                "nodes": self.nodes
            }
            data["flow"]["head_node_id"] = self.head_node_id
            json.dump(data, file, indent=4)

    def validateFlow(self, data):

        # 0.必须包含meta
        if not data.get("meta"):
            # raise ValueError("JSON must contain 'meta'")
            print("必须包含meta")
            return False

        # 1.必须包含flow
        if not data.get("flow"):
            # raise ValueError("JSON must contain 'flow'")
            print("必须包含flow")
            return False
        
        # 2.必须包含cmds
        if not data.get("cmds"):
            # raise ValueError("JSON must contain 'cmds'")
            print("必须包含cmds")
            return False

        # 3.必须包含nodes
        if not data.get("nodes"):
            # raise ValueError("JSON must contain 'nodes'")
            print("必须包含nodes")
            return False

        # 1.必须包含head_node_id
        flow = data.get("flow")
        if not flow.get("head_node_id"):
            # raise ValueError("JSON must contain 'head_node_id'")
            print("必须包含head_node_id")
            return False

        # 通过验证
        return True


    '''
    指令操作
    '''
    def loadCmds(self):
        for key, cmd in self.cmds.items():
            self.cmdObjs[key] = Cmd(cmd)

    def getCmd(self, cmd_id):
        return self.cmdObjs.get(cmd_id)
    
    def addCmd(self, cmd):
        pass
    
    def delCmd(self, cmd):
        pass

    def delCmdLink(self, cmd):
        pass
    
    def setCmd(self, cmd):
        pass

    '''
    视图操作
    '''
    
    def genQmlModel(self):
        nodes_model = []
        connections_model = []

        for key in self.nodes:
            # print(key)
            nodes_model.append({"id": key, "text": self.cmds[key]['name'], "x": self.nodes[key]["x"], "y": self.nodes[key]["y"]})
            for child in self.flow[key]:
                connections_model.append({"from": key, "to": child})

        # print("Nodes model:", nodes_model)
        # print("Connections model:", connections_model)
        return nodes_model, connections_model

    '''
    核心操作
    '''
    def start(self):
        self.cursor = self.head_node_id
        theCmd = self.getCmd(self.cursor)
        asyncio.run(theCmd.run())
        if theCmd.status == 2:
            next_cmd_count = len(self.flow[self.cursor])
            while(next_cmd_count>0):
                
                if next_cmd_count==1:
                    self.cursor = self.flow[self.cursor][0]
                    theCmd = self.getCmd(self.cursor)
                    asyncio.run(theCmd.run())     
                    if theCmd.status == 2:
                        next_cmd_count = len(self.flow[self.cursor])  
                    else:
                        print(f"指令 {self.cursor} 执行失败")
                        self.flowStatus = 4  # Set status to error
                        break         
                else:
                    print(f"指令 {self.cursor} 有多条路径, 请手动选择")
                    next_cmd_count = 1
        else:
            print(f"指令 {self.cursor} 执行失败")
            self.flowStatus = 4  # Set status to error
        
        print(f"指令 {self.cursor} 执行完成")

    def stop(self, name):
        cmd = self.get_cmd(name)
        if cmd:
            return cmd.stop()
        else:
            raise ValueError(f"Command {name} not found.")

    def pause(self, name):
        cmd = self.get_cmd(name)
        if cmd:
            return cmd.pause()
        else:
            raise ValueError(f"Command {name} not found.")

    def goon(self, name):
        cmd = self.get_cmd(name)
        if cmd:
            return cmd.goon()
        else:
            raise ValueError(f"Command {name} not found.")


class Cmd:

    def __init__(self, cmd_dict):
        self.type = cmd_dict.get("type")
        self.name = cmd_dict.get("name")
        self.param = cmd_dict.get("param")
        self.monitor = cmd_dict.get("monitor")
        self.status = 0  # 0: idle, 1: running, 2: done, 3: error
        self.beginTime = ""
        self.endTime = ""
        self.result = None

    async def run(self):

        if (self.status != 0):
            raise RuntimeError("无法运行非空闲状态指令!")

        self.status = 1  # Set status to running
        self.beginTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Set start time in "yyyy-mm-dd hh:mm:ss" format
        try:
            print(f"正在执行指令: {self.name}")
            await asyncio.sleep(3)  # Use 'duration' from params or default to 1 second
            self.result = "success"  # Set result after process completion
            self.status = 2  # Set status to done
        except Exception as e:
            self.result = str(e)  # Capture exception as result
            self.status = 3  # Set status to error
        finally:
            self.endTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Replace with actual end time logic
            print(f"Command {self.name} finished with result: {self.result}")


