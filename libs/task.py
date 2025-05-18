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
        self.status = kwargs.get('status', 0)  # Default to idle
        self.startTime = kwargs.get('startTime', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.endTime = kwargs.get('endTime', None)
        self.reseted = kwargs.get('reseted', False)

        # clone the CmdManager not reference
        self.theCmdManager = deepcopy(theCmdManager)

        # Initialize other properties
        self.columns = self.getColumns(self.carType)
        self.values = self.getValues(self.carType)

        # Set initial status from CmdManager if available
        if self.theCmdManager:
            self.status = self.theCmdManager.flowStatus

    def getColumns(self, carType):
        # 从数据库中获取列信息
        return ["任务ID", "数据名称", "数值", "最小值", "最大值", "是否合格"]

    def getValues(self, carType):
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

        # Register a callback to update task status when flow completes
        def update_status():
            self.status = self.theCmdManager.flowStatus
            if self.status in [2, 3, 4]:  # If completed, stopped, or error
                self.endTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Add the callback to the CmdManager
        self.theCmdManager.register_callback(update_status)
