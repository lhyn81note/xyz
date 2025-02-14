from dependency_injector import containers, providers
from .device.plc import ModbusTcp
from .utils import impmod, enum2names
from .notify import MsgType, MsgBroker, MsgSubscriber
from .dbhelper import GenDbEnging

print(f"{' Libs ':#^50}")

class Utils(containers.DeclarativeContainer):
    impmod = providers.Factory(impmod)
    enum2names = providers.Factory(enum2names)

class Devices(containers.DeclarativeContainer):
    modbusTcp = providers.Singleton(ModbusTcp)

class Notify(containers.DeclarativeContainer):
    msgBroker = providers.Singleton(MsgBroker)
    msgSubscriber = providers.Factory(MsgSubscriber)

genDbEnging = GenDbEnging