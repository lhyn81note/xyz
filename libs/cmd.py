import asyncio
from datetime import datetime
import json
import time
import threading
from PySide6.QtCore import QObject, Signal, Slot

class CmdMananger(QObject):

    evtCmdChanged = Signal(str, int)  # Signal to emit status changes with id and status
    evtPopup = Signal(str, dict)  # Signal to request path selection (current_node, paths, cmd_names)

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

        with open(self.flow_file, 'r', encoding='utf-8') as file:

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
            print(f'保存{self.flow_file}')
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
            newCmd = Cmd(key, cmd)
            newCmd.evtStatusChanged.connect(self.onChildStatusChanged)
            self.cmdObjs[key] = newCmd

    def getCmd(self, cmd_id):
        return self.cmdObjs.get(cmd_id)

    def addCmd(self, cmd):
        pass

    def delCmd(self, cmd):
        pass

    def delCmdChain(self, cmd):
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
            nodes_model.append({
                "id": key, 
                "text": self.cmds[key]['name'], 
                "x": self.nodes[key]["x"], 
                "y": self.nodes[key]["y"],
                "type": self.cmds[key]['type']
            })
            
            for child in self.flow[key]:
                connections_model.append({"from": key, "to": child})

        # print("Nodes model:", nodes_model)
        # print("Connections model:", connections_model)
        return nodes_model, connections_model
        

    def run_flow(self):
        
        def job():
            """Run the flow asynchronously."""
            self.cursor = self.head_node_id
            self.flowStatus = 0  # Reset flow status

            theCmd = self.getCmd(self.cursor)
            theCmd.run(self.plc)

            if theCmd.status == 2:
                next_cmd_count = len(self.flow[self.cursor])

                while next_cmd_count > 0:

                    if next_cmd_count == 1:
                        self.cursor = self.flow[self.cursor][0]

                    else:
                        path_names = list(map(lambda cmdkey: f'{cmdkey}:{self.cmds[cmdkey]['name']}', self.flow[self.cursor]))
                        self.popper.evtBegin.emit("路径选择弹窗",{
                            "next":path_names
                        })

                        while self.popper.done == False:
                            time.sleep(1)

                        self.popper.done = False
                        self.cursor = self.popper.result.split(":")[0]

                    print(self.cursor)
                    if self.cursor==None:
                        print("路径为空,流程中断")
                        self.flowStatus = 3
                        break

                    # 执行指针指令
                    theCmd = self.getCmd(self.cursor)
                    theCmd.run(self.plc)

                    if theCmd.status == 2:
                        next_cmd_count = len(self.flow[self.cursor])
                    else:
                        print(f"流指令 {self.cursor} 执行失败")
                        self.flowStatus = 4  # Set status to error
                        break


            else:
                print(f"流指令 {self.cursor} 执行失败")
                self.flowStatus = 4  # Set status to error

            if self.flowStatus == 4:
                print(f'有故障,流程中断')
            else:
                print(f'流程执行完毕')

            return self.flowStatus
    
        thread = threading.Thread(target=job, daemon=True)
        thread.start()

    def run_step(self, theCmd):
        """Start a single step execution in a background thread."""
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
        self.status = 0  # 0: idle, 1: running, 2: done, 3: error
        self.beginTime = ""
        self.endTime = ""
        self.result = None

    @property
    def duration(self):
        if self.beginTime and self.endTime:
            begin = datetime.strptime(self.beginTime, "%Y-%m-%d %H:%M:%S")
            end = datetime.strptime(self.endTime, "%Y-%m-%d %H:%M:%S")
            return (end - begin).total_seconds()
        return None


    def run(self, plc):

        def run_sys(self):
            time.sleep(1)
            self.result = "sys done."
            self.status = 2  # Set status to done

        def run_plc(self, plc):
            pt_out = plc.pts.get(self.param.get("out"))
            pt_args = self.param.get("args")
            pt_cmd = plc.pts.get(self.param.get("out")) # 取得plc点表中的实例
            pt_sig_name = pt_cmd.done[0]  # 取得plc点表中的monitor覆盖当前cmd的monitor
            pt_sig = plc.pts.get(pt_sig_name)

            for arg_kv in pt_args:
                print(f"写入指令: {arg_kv}")
                for k,v in arg_kv.items():
                    print(f"写入指令: {k} = {v}")
                    pt_arg = plc.pts.get(k)
                    if pt_arg is None:
                        print(f"指令不存在!{k}")
                        return False
                    else:
                        plc.write(k, v)

            plc.write(pt_out.id, 1)
            while self.status == 1:
                time.sleep(plc.interval/1000)
                # print(pt_sig)
                for k in plc.pts.keys():
                    if 'alarm' in k:
                        # print(f"capture:{plc.pts.get(k)}")0
                        if plc.pts.get(k).value==True:
                            self.result = "plc fault."
                            self.status = 3  # Set status to done
                            break

                if pt_sig.value == 1:
                    print(f"监控点 {pt_sig.id} 触发!!!")
                    self.result = "plc done."
                    self.status = 2  # Set status to done
                    break
                # await asyncio.sleep(1)


        if (self.status != 0):
            raise RuntimeError("无法运行非空闲状态指令!")

        self.status = 1  # Set status to running
        self.beginTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Set start time in "yyyy-mm-dd hh:mm:ss" format
        self.evtStatusChanged.emit(self.id, self.status)

        try:
            if self.type == "sys":
                run_sys(self)

            elif self.type == "plc":
                run_plc(self, plc)

        except Exception as e:
            self.result = str(e)  # Capture exception as result
            self.status = 3  # Set status to error

        finally:
            self.endTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Replace with actual end time logic
            self.evtStatusChanged.emit(self.id, self.status)
            print(f"指令 {self.name} 执行完毕: {self.result}")