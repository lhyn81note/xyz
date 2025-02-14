
from libs.device import MODBUS_AREA, MODBUS_VARTYPE, BYTE_ENDIAN, WORD_ENDIAN, IO

plc_setting = {
    'host':'127.0.0.1',
    'port':502,
    'timeout':5,
    'interval':0.5,
    'byte_order': BYTE_ENDIAN.BIG,
    'word_order': WORD_ENDIAN.BIG,
    'pts':[
        {"io":IO.IN, "slave":1, "area":MODBUS_AREA.Coil, "address":"0.1", "type":MODBUS_VARTYPE.Bool, "name":"测试点1", "value":"null"},
        {"io":IO.IN, "slave":1, "area":MODBUS_AREA.InCoil, "address":"0.1", "type":MODBUS_VARTYPE.Bool, "name":"测试点2", "value":"null"},
        {"io":IO.IN, "slave":1, "area":MODBUS_AREA.Reg, "address":"0.4", "type":MODBUS_VARTYPE.Bool, "name":"测试点3", "value":"null"},
        {"io":IO.IN, "slave":1, "area":MODBUS_AREA.Reg, "address":"2", "type":MODBUS_VARTYPE.Int_16, "name":"测试点6", "value":"null"},
        {"io":IO.IN, "slave":1, "area":MODBUS_AREA.Reg, "address":"3", "type":MODBUS_VARTYPE.Int_32, "name":"测试点8", "value":"null"},
        {"io":IO.IN, "slave":1, "area":MODBUS_AREA.Reg, "address":"10", "type":MODBUS_VARTYPE.Real_32, "name":"测试点10", "value":"null"},
        {"io":IO.OUT, "slave":1, "area":MODBUS_AREA.Coil, "address":"0.3", "type":MODBUS_VARTYPE.Bool, "name":"测试点13", "value":"null"},
        {"io":IO.OUT, "slave":1, "area":MODBUS_AREA.Reg, "address":"15", "type":MODBUS_VARTYPE.Int_16, "name":"测试点14", "value":"null"},
        {"io":IO.OUT, "slave":1, "area":MODBUS_AREA.Reg, "address":"16", "type":MODBUS_VARTYPE.Int_32, "name":"测试点15", "value":"null"},
        {"io":IO.OUT, "slave":1, "area":MODBUS_AREA.Reg, "address":"18", "type":MODBUS_VARTYPE.Real_32, "name":"测试点16", "value":"null"},
        {"io":IO.OUT, "slave":1, "area":MODBUS_AREA.Reg, "address":"18", "type":MODBUS_VARTYPE.Real_32, "name":"测试点16", "value":"null"},
    ],
}