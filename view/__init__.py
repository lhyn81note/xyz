from .frame.view import Window as MainFrame
from .graph.view import Window as view_graph
from .plcs.view import Window as view_plc
from .db_users.view import Window as view_db_user
from .db_basic.view import Window as view_db_basic
from .db_types.view import Window as view_db_types
from .login.view import LoginWindow

Views = {
    'view_index':{'title':'自动流程','obj':view_graph},
    'view_plc':{'title':'PLC功能测试','obj':view_plc},
    'view_db_user':{'title':'用户设置','obj':view_db_user},
    'view_db_basic':{'title':'基本参数设置','obj':view_db_basic},
    'view_db_types':{'title':'转向架类型设置','obj':view_db_types},
}
print(f"{' Views ':#^50}")

Menus = {
    '试验操作':[
        {'title':'PLC实时监控', 'icon':'plc.png', 'view_id':'view_plc','pop':False, 'fixed':False},
    ],
    '设置':[
        {'title':'用户设置', 'icon':'db.png', 'view_id':'view_db_user','pop':False, 'fixed':False},
        {'title':'转向架类型设置', 'icon':'db.png', 'view_id':'view_db_basic','pop':False, 'fixed':False},
        {'title':'基础数据设置', 'icon':'db.png', 'view_id':'view_db_types','pop':False, 'fixed':False},
    ],
}
print(f"{' Menus ':#^50}")