import asyncio
from datetime import datetime
import json
from PySide6.QtCore import QObject, Signal, Slot
import threading

class CmdMananger(QObject):

    evtCmdChanged = Signal(str, int)  # Signal to emit status changes with id and status
    evtPopup = Signal(str, dict)  # Signal to request path selection (current_node, paths, cmd_names)

    def __init__(self, flow_file, plc):

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

        self.popup_callback = None

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
            nodes_model.append({"id": key, "text": self.cmds[key]['name'], "x": self.nodes[key]["x"], "y": self.nodes[key]["y"]})
            for child in self.flow[key]:
                connections_model.append({"from": key, "to": child})

        # print("Nodes model:", nodes_model)
        # print("Connections model:", connections_model)
        return nodes_model, connections_model

    '''
    核心操作
    '''
    async def popup(self, dialog_id=None, args=None):

        future = asyncio.Future()
        print(id(future))

        # Define a callback to set the Future result
        def onReturn(results):
            # if not future.done():
            future.set_result(results)
            # future.done()
            print(id(future))
            print("Return!!!")
            return True


        # We need to use the main thread to create and show the dialog
        # This is done by emitting a signal that the main thread will handle
        self.evtPopup.emit("test",{
            "dialog_id": "abc",
            "args": "123"
        })

        # Store the callback for the main thread to call
        self.popup_callback = onReturn

        # Wait for the result with a timeout
        result = await future  # 5 minutes timeout
        print("路径选择结果:", result)
        return result
        

    async def run_flow_async(self):
        """Run the flow asynchronously."""
        self.cursor = self.head_node_id
        self.flowStatus = 0  # Reset flow status

        theCmd = self.getCmd(self.cursor)
        await theCmd.run_async(self.plc)

        if theCmd.status == 2:
            next_cmd_count = len(self.flow[self.cursor])
            while next_cmd_count > 0:
                if next_cmd_count == 1:
                    # Only one path, take it automatically
                    self.cursor = self.flow[self.cursor][0]
                    theCmd = self.getCmd(self.cursor)
                    await theCmd.run_async(self.plc)

                    if theCmd.status == 2:
                        next_cmd_count = len(self.flow[self.cursor])
                    else:
                        print(f"流指令 {self.cursor} 执行失败")
                        self.flowStatus = 4  # Set status to error
                        break
                else:
                    # Multiple paths, request user selection
                    print(f"流指令 {self.cursor} 有多条路径, 请求用户选择")
                    self.evtPopup.emit("test",{
                        "dialog_id": "abc",
                        "args": "123"
                    })

        else:
            print(f"流指令 {self.cursor} 执行失败")
            self.flowStatus = 4  # Set status to error

        if self.flowStatus == 4:
            print(f'有故障,流程中断')
        else:
            print(f'流程执行完毕')

        return self.flowStatus

    def runflow(self):
        """Start the flow execution in a background thread."""
        def run_flow_wrapper():
            asyncio.run(self.run_flow_async())

        thread = threading.Thread(target=run_flow_wrapper)
        thread.start()

    async def run_step_async(self, theCmd):
        """Run a single step asynchronously."""
        await theCmd.run_async(self.plc)
        if theCmd.status == 2:
            print(f"单步指令 {theCmd.name} 执行成功")
        else:
            print(f"单步指令 {theCmd.name} 执行失败")
        return theCmd.status

    def runstep(self, theCmd):
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


    async def run_async(self, plc):

        async def run_sys(self):
            await asyncio.sleep(1)
            self.result = "sys done."
            self.status = 2  # Set status to done

        async def run_plc(self, plc):
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
                await asyncio.sleep(plc.interval/1000)
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
                await run_sys(self)

            elif self.type == "plc":
                await run_plc(self, plc)

        except Exception as e:
            self.result = str(e)  # Capture exception as result
            self.status = 3  # Set status to error

        finally:
            self.endTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Replace with actual end time logic
            self.evtStatusChanged.emit(self.id, self.status)
            print(f"指令 {self.name} 执行完毕: {self.result}")