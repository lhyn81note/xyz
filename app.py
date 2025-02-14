import sys
from PySide6.QtWidgets import QApplication
from setting import *
from libs import *
from models import *
from wgts import TabWidget, PlcData, PlcTable
from view import Views, Menus, MainFrame

# 全局Service初始化
LibServices = Utils()
Broker = Notify().msgBroker()
PLC = Devices().modbusTcp()

# 全局数据库引擎初始化
DbEng_Alarms = GenDbEnging(dbpath="sqlite:///db/Alarms.db")
DbEng_AlarmsCode = GenDbEnging(dbpath="sqlite:///db/AlarmsCode.db")
DbEng_BaseData = GenDbEnging(dbpath="sqlite:///db/BaseData.db")
DbEng_Log = GenDbEnging(dbpath="sqlite:///db/Log.db")
DbEng_model = GenDbEnging(dbpath="sqlite:///db/model.db")
DbEng_result = GenDbEnging(dbpath="sqlite:///db/result.db")
DbEng_user = GenDbEnging(dbpath="sqlite:///db/user.db")

# 全局数据表模型初始化
TblUser = TblUser(engine=DbEng_user)

FaultCode = FaultCode(engine=DbEng_AlarmsCode)
FaultLog = FaultLog(engine=DbEng_Alarms)
Log = Log(engine=DbEng_Log)

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
    PLC.init(config=plc_setting)
    PLC.conn()
    PLC.loop()
    PLC.start()
    main_win = MainFrame(menus=Menus, title="QtAppX")
    main_win.show()
    sys.exit(app.exec())