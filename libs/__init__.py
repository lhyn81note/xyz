from dependency_injector import containers, providers

from .cmd import CmdMananger, Cmd
from .device.plc_s7 import S7
# from .device.plc_modbus import ModbusTcp

from .utils import impmod, enum2names
from .notify import MsgType, MsgBroker, MsgSubscriber
from .dbhelper import GenDbEnging

print(f"{' Libs ':#^50}")

class CoreProvider(containers.DeclarativeContainer):
    CmdManager = providers.Singleton(CmdMananger)
    Cmd = providers.Factory(Cmd)
    Plc = providers.Singleton(S7)
    MsgBroker = providers.Singleton(MsgBroker)
    MsgSubscriber = providers.Factory(MsgSubscriber)

class UtilsProvider(containers.DeclarativeContainer):
    Impmod = providers.Factory(impmod)
    Enum2names = providers.Factory(enum2names)
