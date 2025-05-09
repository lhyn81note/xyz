from abc import abstractmethod, ABCMeta
from typing import List, Dict, TypeVar, Union
from enum import Enum
from ..notify import MsgType, MsgBroker, MsgSubscriber

__all__ = ["BasePlc", "plc_modbus", "plc_s7"]

T=TypeVar("T")

class BasePlc(metaclass = ABCMeta):

    def __init__(self):
        self.pts_file_path = None
        self.addr =     None
        self.protocal = None
        self.interval = None
        self.client_r = None
        self.client_w = None
        self.pts = {}
        self.callbacks = []  # 用于存储回调函数
        self.msgbroker = None

    @property
    def alive(self)->bool:
        try:
            return self.client_r.get_connected() and self.client_w.get_connected()
        except Exception as e:
            return False

    def register_callback(self, callback):
        if callable(callback):
            self.callbacks.append(callback)
        else:
            raise ValueError("无法调用对象")

    def trigger_callbacks(self, *args, **kwargs):
        for callback in self.callbacks:
            if callback is not None:
                callback(*args, **kwargs)

    @abstractmethod
    def load_config(self)->bool:
        pass

    @abstractmethod
    def connect(self)->bool:
        pass

    @abstractmethod
    def read(self, ptId) -> bool :
        pass

    @abstractmethod
    def write(self, ptId) -> bool :
        pass

    @abstractmethod
    def scan(self) -> bool :
        pass