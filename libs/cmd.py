import asyncio
from datetime import datetime
import json
import time
import threading
import uuid
import logging
from PySide6.QtCore import QObject, Signal, Slot

# 导入所有的弹窗类
from .algos.wait import algoWait
from .algos.summary import algoSummary
from .algos.statics import algoStatics

# 弹窗表映射
algoMap = {
    "algoWait": algoWait,
    "algoSummary": algoSummary,
    "algoStatics": algoStatics,
}


class CmdManager(QObject):

    evtCmdChanged = Signal(str, int)  # Signal to emit status changes with id and status
    evtPopup = Signal(str, dict)  # Signal to request path selection (current_node, paths, cmd_names)
    evtFlowStatusChanged = Signal(int)

    def __init__(self, flow_file, plc, popper):

        super().__init__()
        self.flow_file = flow_file
        self.plc = plc
        self.meta = {}

        self.head_node_id = None  # Placeholder for head node ID
        self.flow = {}  # Placeholder for flow configuration

        self.cmds = {}
        self.cmdObjs = {}

        self.nodes = {}

        self.cursor = ""  # Placeholder for flow configuration
        self.flowStatus = 0  # 0: idle, 1: running, 2: paused, 3: stopped 4: error

        self.popper = popper

        # 初始化
        self.loadFlow()
        self.loadCmds()

    @Slot(str, int)
    def onChildStatusChanged(self, id, status):
        self.evtCmdChanged.emit(id, status)

    '''
    流程配置文件操作
    '''
    def loadFlow(self) -> bool:

        with open(self.flow_file, 'r', encoding='gbk') as file:

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
            json.dump(data, file, indent=4, ensure_ascii=False)

    def validateFlow(self, data):

        # 0.必须包含meta
        if not data.get("meta"):
            # raise ValueError("JSON must contain 'meta'")
            return False

        # 1.必须包含flow
        if not data.get("flow"):
            logging.error("flow配置文件缺少meta")
            return False

        # 2.必须包含cmds
        if not data.get("cmds"):
            logging.error("flow配置文件缺少cmds")
            return False

        # 3.必须包含nodes
        if not data.get("nodes"):
            logging.error("flow配置文件缺少nodes")
            return False

        # 1.必须包含head_node_id
        flow = data.get("flow")
        if not flow.get("head_node_id"):
            logging.error("flow配置文件缺少head_node_id")
            return False

        # 通过验证
        return True
    
    def reset(self):
        for cmd in self.cmdObjs.values():
            cmd.cmdStatus = 0
            cmd.evtStatusChanged.emit(cmd.id, cmd.cmdStatus)


    '''
    指令操作
    '''
    def loadCmds(self):
        for key, cmd in self.cmds.items():
            newCmd = Cmd(key, cmd)
            newCmd.evtStatusChanged.connect(self.onChildStatusChanged)
            self.cmdObjs[key] = newCmd

    def getCmd(self, cmd_id):
        return self.cmdObjs.get(cmd_id)

    def addCmd(self, parent_id):
        # Generate a new UUID for the new command
        new_cmd_id = str(uuid.uuid4())[:8]

        # Create a new empty command with type "algo"
        new_cmd = {
            "type": "algo",
            "name": "空指令",
            "param": {
                "funcID":"algoWait",
                "args": 1,
                "done": None
            }
        }

        # Add the new command to the cmds dictionary
        self.cmds[new_cmd_id] = new_cmd

        # Add the new command to the flow as a child of the parent command
        if parent_id in self.flow:
            self.flow[parent_id].append(new_cmd_id)
        else:
            self.flow[parent_id] = [new_cmd_id]

        # Initialize the flow for the new command (empty list of children)
        self.flow[new_cmd_id] = []

        # Calculate position for the new node based on parent node
        parent_x = self.nodes[parent_id]["x"]
        parent_y = self.nodes[parent_id]["y"]

        # Position the new node slightly to the right and below the parent
        new_x = parent_x + 15
        new_y = parent_y + 15

        # Add the new node to the nodes dictionary
        self.nodes[new_cmd_id] = {
            "x": new_x,
            "y": new_y,
            "text": "空指令",
            "status": "idle"
        }

        # Create a new Cmd object and add it to cmdObjs
        newCmd = Cmd(new_cmd_id, new_cmd)
        newCmd.evtStatusChanged.connect(self.onChildStatusChanged)
        self.cmdObjs[new_cmd_id] = newCmd

        # Save the updated flow to the JSON file
        self.saveFlow()
        self.loadFlow()
        self.loadCmds()

    def delCmd(self, cmd):
        self.saveFlow()
        self.loadFlow()
        self.loadCmds()


    def setCmd(self, cmd_id, child_id):
        self.flow[cmd_id] = [child_id]
        self.saveFlow()
        self.loadFlow()
        self.loadCmds()

    '''
    视图操作
    '''

    def genQmlModel(self):
        nodes_model = []
        connections_model = []

        for key in self.nodes:
            nodes_model.append({
                "id": key, 
                "text": self.cmds[key]['name'], 
                "x": self.nodes[key]["x"], 
                "y": self.nodes[key]["y"],
                "type": self.cmds[key]['type']
            })
            
            for child in self.flow[key]:
                connections_model.append({"from": key, "to": child})

        return nodes_model, connections_model
        

    def run_flow(self):
        
        logging.info(f"########### 开始执行流程<{self.meta['name']}>")
        def job():
            self.cursor = self.head_node_id
            self.flowStatus = 1  # Reset flow status

            # 执行第一条指令
            theCmd = self.getCmd(self.cursor)
            theCmd.run(input=None, plc=self.plc, top_popper=self.popper)

            # 第一条指令执行完毕
            if theCmd.cmdStatus == 2:

                next_cmd_count = len(self.flow[self.cursor]) # 计算下一步指令数量, 0表示end, 1表示下一步, 2表示下一步多个

                # 开始执行下一条指令, 直到end
                while next_cmd_count > 0:

                    # 整体异常捕获
                    try:

                        if next_cmd_count == 1:
                            self.cursor = self.flow[self.cursor][0]

                        else:
                            path_names = list(map(lambda cmdkey: f'{cmdkey}:{self.cmds[cmdkey]['name']}', self.flow[self.cursor]))
                            self.popper.evtBegin.emit(
                                "dialogPath",
                                {
                                "next_cmds":path_names
                                },
                                None # last input is not used here
                            )

                            while self.popper.done == False:
                                time.sleep(1)

                            self.popper.done = False
                            self.cursor = self.popper.result.split(":")[0]

                        if self.cursor==None: # 这里指令还为空说明有问题
                            logging.error("执行错误:此处指令不应该为None")
                            self.flowStatus = 4
                            break

                        # 这里已经获取到下一步指令指针了
                        lastCmdResult = theCmd.result # 先保存上一步指令结果
                        theCmd = self.getCmd(self.cursor) # 切换指令
                        theCmd.run(input=lastCmdResult, plc=self.plc, top_popper=self.popper)

                        if theCmd.cmdStatus == 2: # 如果当前指令执行成功
                            next_cmd_count = len(self.flow[self.cursor])
                        else: # 如果当前指令执行失败
                            logging.error(f"流程异常:指令执行返回2")
                            self.flowStatus = 4 
                            break
                
                    except Exception as e:
                        logging.error(f"流程异常:异常原因:{e}")
                        self.flowStatus = 4
                        break
                
                if self.flowStatus == 1:
                    self.flowStatus = 2 # 正常执行完毕, 状态为2
                    
                    
            else:
                logging.error(f"流程异常:第一条指令状态应为2")
                self.flowStatus = 4  # Set status to error

            if self.flowStatus == 2:
                logging.info(f'########### 流程执行完毕<{self.meta['name']}>')
            elif  self.flowStatus == 3:
                logging.info(f'########### 流程执行被停止<{self.meta['name']}>')
            else:
                logging.info(f'########### 流程执行结束,但状态异常<{self.meta['name']}>')

            self.evtFlowStatusChanged.emit(self.flowStatus)
            return self.flowStatus
    
        thread = threading.Thread(target=job, daemon=True)
        thread.start()

    def run_step(self, theCmd):
        def run_step_wrapper():
            asyncio.run(self.run_step_async(theCmd))

        thread = threading.Thread(target=run_step_wrapper)
        thread.start()

    def stop(self, name):
        pass

    def pause(self, name):
        pass

    def goon(self, name):
        pass


class Cmd(QObject):

    evtStatusChanged = Signal(str, int)  # Signal to emit status changes with id and status
    evtCmdNotify = Signal(str, dict) 

    def __init__(self, id, cmd_dict):
        super().__init__()
        self.id = id
        self.type = cmd_dict.get("type")
        self.name = cmd_dict.get("name")
        self.param = cmd_dict.get("param")
        self.cmdStatus = 0  # 0: idle, 1: running, 2: done, 3: error
        self.beginTime = ""
        self.endTime = ""
        self.result = None

    @property
    def duration(self):
        if self.beginTime and self.endTime:
            begin = datetime.strptime(self.beginTime, "%Y-%m-%d %H:%M:%S")
            end = datetime.strptime(self.endTime, "%Y-%m-%d %H:%M:%S")
            return (end - begin).total_seconds().__round__(2)
        return None


    def run(self, input=None, plc=None, top_popper=None):

        def run_algo(self):
            logging.info(f">>> 开始执行指令: 名称<{self.name}> 类型<algo> 算法类型:<{self.param.get('funcID')}>")
            # Algo类型Cmd的结果为Algo返回值
            self.result = algoMap[self.param.get("funcID")](self.param.get("args"), input=input)
            self.cmdStatus = 2

        def run_pop(self):
            logging.info(f">>> 开始执行指令: 名称<{self.name}> 类型<pop> 弹窗类型:<{self.param.get('funcID')}>")
            top_popper.evtBegin.emit(
                self.param["funcID"], 
                self.param["args"],
                input)

            while top_popper.done == False:
                time.sleep(1)

            top_popper.done = False
            self.result = top_popper.result # Pop类型Cmd的结果为弹窗内部结果(这里result已经被赋值了)
            self.cmdStatus = 2

        def run_plc(self):
            logging.info(f">>> 开始执行指令: 名称<{self.name}> 类型<plc> 动作:<{self.param.get('out')}>")
            self.result = None # plc类型的结果为None,只看status
            pt_out = plc.pts.get(self.param.get("out"))
            pt_args = self.param.get("args")
            pt_sig_name = pt_out.done[0]  # 取得plc点表中的monitor覆盖当前cmd的monitor
            pt_sig = plc.pts.get(pt_sig_name)

            # 写参数
            for arg_kv in pt_args:
                for k,v in arg_kv.items():
                    pt_arg = plc.pts.get(k)
                    if pt_arg is None:
                        logging.error(f"指令<{k}>不存在!")
                        return False
                    else:
                        plc.write(k, v)
            
            # 启动指令
            plc.write(pt_out.id, 1)

            # 监控完成
            while self.cmdStatus == 1:
                time.sleep(plc.interval/1000)
                for k in plc.pts.keys():
                    if 'alarm' in k:
                        if plc.pts.get(k).value==True:
                            self.cmdStatus = 3  # Set status to done
                            break
                
                # 完成了!
                if pt_sig.value == 1:
                    self.cmdStatus = 2  # Set status to done
                    break

        if (self.cmdStatus != 0):
            logging.error("无法运行非空闲状态指令!")
            raise RuntimeError("无法运行非空闲状态指令!")

        # 设定状态为运行中
        self.cmdStatus = 1  # Set status to running
        self.beginTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Set start time in "yyyy-mm-dd hh:mm:ss" format
        self.evtStatusChanged.emit(self.id, self.cmdStatus)

        try:
            if self.type == "algo":
                run_algo(self)

            elif self.type == "pop":
                run_pop(self)

            elif self.type == "plc":
                run_plc(self)

            else:
                logging.error(f"指令类型不对<{self.type}>")
                raise RuntimeError(f"指令类型不对<{self.type}>")

        except Exception as e:
            self.result = str(e)  # Capture exception as result
            self.cmdStatus = 3  # Set status to error

        finally:
            self.endTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Replace with actual end time logic
            self.evtStatusChanged.emit(self.id, self.cmdStatus)
            logging.info(f"<<< 指令<{self.name}> 执行完毕 ---> 执行结果:{self.result}")