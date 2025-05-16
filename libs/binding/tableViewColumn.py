#表列表定义类
class TableViewColumn:
    #初始化 表头，列宽，列高，对齐方式，是否只读，控件类型，绑定
    def __init__(self, header, width, height, align, isReadOnly, widget_type,bind):
        self.header = header
        self.width = width
        self.height = height
        self.align = align
        self.widget_type = widget_type
        self.isReadOnly = isReadOnly
        self.bind = bind
       