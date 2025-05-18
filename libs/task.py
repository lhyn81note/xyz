import uuid
import datetime
from copy import deepcopy
from typing import List, Optional, Dict, Any

# Create a simple Task class without using Pydantic
class Task:
    def __init__(self, carType: str, workerId: str, theCmdManager=None, **kwargs):
        # Set basic attributes
        self.taskId = kwargs.get('taskId', str(uuid.uuid4())[:8])  # 8 character UUID
        self.carType = carType
        self.workerId = workerId
        self.startTime = kwargs.get('startTime', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.endTime = kwargs.get('endTime', None)
        self.reseted = kwargs.get('reseted', False)

        @property
        def status(self):
            return self.theCmdManager.flowStatus

        # clone the CmdManager not reference
        self.theCmdManager = theCmdManager

        # Initialize other properties
        self.columns = self.getColumns()
        self.values = self.getValues()

        # Set initial status from CmdManager if available
        if self.theCmdManager:
            self.status = self.theCmdManager.flowStatus

    def getColumns(self):
        # 从数据库中获取列信息
        return ["序号", "数据名称", "数值", "最小值", "最大值", "是否合格"]

    def getValues(self):
        # 从数据库中获取值信息
        return ["测试数据1", "测试数据2", "测试数据3"]

    def startTask(self):
        """Start the task by resetting and running the flow"""
        if not self.theCmdManager:
            print("Error: No CmdManager available")
            return

        # Reset the flow first
        self.theCmdManager.reset()

        # Update task status and start time
        self.status = 1  # Set to running
        self.startTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.endTime = None

        # Run the flow
        self.theCmdManager.run_flow()
