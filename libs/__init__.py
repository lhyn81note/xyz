from dependency_injector import containers, providers

from .device.plc_s7 import S7
# from .device.plc_modbus import ModbusTcp

from .utils import impmod, enum2names
from .notify import MsgType, MsgBroker, MsgSubscriber
from .dbhelper import GenDbEnging

print(f"{' Libs ':#^50}")

class Utils(containers.DeclarativeContainer):
    impmod = providers.Factory(impmod)
    enum2names = providers.Factory(enum2names)

class Devices(containers.DeclarativeContainer):
    Plc = providers.Singleton(S7)

class Notify(containers.DeclarativeContainer):
    msgBroker = providers.Singleton(MsgBroker)
    msgSubscriber = providers.Factory(MsgSubscriber)

genDbEnging = GenDbEnging