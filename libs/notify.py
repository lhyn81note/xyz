from enum import Enum

class MsgType(Enum):
    alarm = "alarm"
    info = "info"
    status = "status"

class MsgBroker:
    def __init__(self):
        self._sublist_alarm = []
        self._sublist_info = []
        self._sublist_status = []
    
    def addSubscriber(self, subscriber, msgtype: MsgType):
        if msgtype == MsgType.alarm:
            self._sublist_alarm.append(subscriber)
        elif msgtype == MsgType.info:
            self._sublist_info.append(subscriber)
        elif msgtype == MsgType.status:
            self._sublist_status.append(subscriber)

    def removeSubscriber(self, subscriber):
        if subscriber in self._sublist_alarm:
            self._sublist_alarm.remove(subscriber)
            return True
        elif subscriber in self._sublist_info:
            self._sublist_info.remove(subscriber)
            return True
        elif subscriber in self._sublist_status:
            self._sublist_status.remove(subscriber)
            return True
        else:
            return False
    
    def publish(self, msgtype, msg):
        if msgtype == MsgType.alarm:
            for subscriber in self._sublist_alarm:
                subscriber.invoke(msg)
        elif msgtype == MsgType.info:
            for subscriber in self._sublist_info:
                subscriber.invoke(msg)
        elif msgtype == MsgType.status:
            for subscriber in self._sublist_status:
                subscriber.invoke(msg)
        else: pass
    
class MsgSubscriber:
    def __init__(self, callback):
        self._callback = callback
    
    def invoke(self, msg):
        if callable(self._callback):
            self._callback(msg)

