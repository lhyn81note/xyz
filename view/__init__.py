from .frame.view import Window as MainFrame

from .index.view import Window as view_index
from .template_notify.view import Window as view_notify
from .template_plc.view import Window as view_plc
from .template_pop.view import Window as view_pop
from .template_bindpage.view import PageBogieModel as view_bind

from .setting_user.view import Window as view_setting_user
from .setting_basic.view import Window as view_setting_basic
from .setting_types.view import Window as view_setting_types

Views = {
    'view_index':{'title':'母版页','obj':view_index},

    'view_notify':{'title':'消息功能测试','obj':view_notify},
    'view_plc':{'title':'PLC功能测试','obj':view_plc},
    'view_pop':{'title':'弹窗测试','obj':view_pop},
    'view_bind':{'title':'控件测试','obj':view_bind},

    'view_setting_user':{'title':'用户设置','obj':view_setting_user},
    'view_setting_basic':{'title':'基本参数设置','obj':view_setting_basic},
    'view_setting_types':{'title':'转向架类型设置','obj':view_setting_types},
}
print(f"{' Views ':#^50}")

Menus = {
    'DEMO':[
        {'title':'PLC功能测试', 'icon':'plc.png', 'view_id':'view_plc','pop':False, 'fixed':False},
        {'title':'消息功能测试', 'icon':'docu.png', 'view_id':'view_notify','pop':False, 'fixed':False},
        {'title':'绑定功能测试', 'icon':'docu.png', 'view_id':'view_bind','pop':False, 'fixed':False},
        {'title':'知识检索', 'icon':'tool.png', 'view_id':'view_pop','pop':True, 'fixed':False},
    ],
    '设置':[
        {'title':'用户设置', 'icon':'db.png', 'view_id':'view_setting_user','pop':False, 'fixed':False},
        {'title':'转向架类型设置', 'icon':'db.png', 'view_id':'view_setting_basic','pop':False, 'fixed':False},
        {'title':'基础数据设置', 'icon':'db.png', 'view_id':'view_setting_types','pop':False, 'fixed':False},
    ],
}
print(f"{' Menus ':#^50}")