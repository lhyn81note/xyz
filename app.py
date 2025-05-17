import sys
import configparser

from PySide6.QtWidgets import QApplication

from libs import *
from models import *
from wgts import TabWidget, PlcData, PlcTable
from view import Views, Menus, MainFrame

import logging

LogConfig.setup_logging()
logger = logging.getLogger(__name__)
logger.info("Application started.")

User="admin"

# 读取程序配置
config = configparser.ConfigParser()
config.read('app.ini')

# 全局容器初始化
Broker = CoreProvider().MsgBroker()
LibServices = UtilsProvider()

# 全局Service初始化
PLC = CoreProvider().Plc(config_file=config.get('plc','pts'), addr=config['plc']['host'], interval=config.getint('plc','interval'), msgbroker=Broker)
PLC.load_config()
PLC.connect()
print(f"PLC连接状态: {PLC.alive}")
PLC.scan()

popper = Popup()  # Create a new instance of PopSignal
Cmd = CoreProvider().Cmd
CmdManager = {}
CmdManager['测试流程'] = CoreProvider().CmdManager(config.get('flow','try_test'), PLC, popper)
CmdManager['气压试验'] = CoreProvider().CmdManager(config.get('flow','try_gas'), PLC, popper)
CmdManager['加载力试验'] = CoreProvider().CmdManager(config.get('flow','try_force'), PLC, popper)


# 全局数据库引擎初始化
DbEng_Alarms = GenDbEnging(dbpath=config.get('db','alarm'))
DbEng_AlarmsCode = GenDbEnging(dbpath=config.get('db','alarmCode'))
DbEng_BaseData = GenDbEnging(dbpath=config.get('db','baseData'))
DbEng_Log = GenDbEnging(dbpath=config.get('db','log'))
DbEng_model = GenDbEnging(dbpath=config.get('db','model'))
DbEng_result = GenDbEnging(dbpath=config.get('db','result'))
DbEng_user = GenDbEnging(dbpath=config.get('db','user'))

# 全局数据表模型初始化
Log = Log(engine=DbEng_Log)
TblUser = TblUser(engine=DbEng_user)
FaultCode = FaultCode(engine=DbEng_AlarmsCode)
FaultLog = FaultLog(engine=DbEng_Alarms)
TblAxesZBase = TblAxesZBase(engine=DbEng_BaseData)
TblPlcCIOmemAbbr =  TblPlcCIOmemAbbr(engine=DbEng_BaseData)
TblSensorBaseValue = TblSensorBaseValue(engine=DbEng_BaseData)
TblSensorData = TblSensorData(engine=DbEng_BaseData)
TblSensorParam = TblSensorParam(engine=DbEng_BaseData)
TblTemplateSize = TblTemplateSize(engine=DbEng_BaseData)
TblBogieCenterPt = TblBogieCenterPt(engine=DbEng_model)
TblBogieLoaderInfo = TblBogieLoaderInfo(engine=DbEng_model)
TblBogiePosi = TblBogiePosi(engine=DbEng_model)
TblBogieTryParamSet = TblBogieTryParamSet(engine=DbEng_model)
TblBogieType = TblBogieType(engine=DbEng_model)
TblTryStreamStatus = TblTryStreamStatus(engine=DbEng_model)
TblBogieResult = TblBogieResult(engine=DbEng_result)
TblNowSheet = TblNowSheet(engine=DbEng_result)
TblResultMx =   TblResultMx(engine=DbEng_result)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_win = MainFrame(menus=Menus, title="QtAppX")
    main_win.show()
    sys.exit(app.exec())