from setting import plc_setting
print(f"{' PLC TEST ':#^50}")
from .plc import ModbusTcp
x=ModbusTcp(config=plc_setting)
x.conn()
print(x)
# Read
for pt in plc_setting['pts'].values():
    x.read_pt(pt)
    print(pt)
# Write
x.write_pt(plc_setting['pts']['v13'],True)
x.write_pt(plc_setting['pts']['v14'],789)
x.write_pt(plc_setting['pts']['v15'],778899)
x.write_pt(plc_setting['pts']['v16'],77.89)
