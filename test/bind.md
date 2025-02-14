graph TD
    A[Bind Package] --> B[核心基类]
    A --> C[控件绑定类]
    A --> D[辅助类]
    
    B --> B1[ControlBaseBinding]
    B --> B2[DtoBase]
    B --> B3[Bind]
    
    C --> C1[按钮类]
    C --> C2[输入框类] 
    C --> C3[列表视图类]
    C --> C4[日期时间类]
    
    D --> D1[ICommand]
    D --> D2[IValueConverter]
    D --> D3[BindingMode]
    D --> D4[Context]

    C1 --> CA[PushButtonBinding]
    C1 --> CB[RadioButtonBinding]
    C1 --> CC[CheckBoxBinding]
    
    C2 --> CD[LineEditBinding]
    C2 --> CE[PlainTextEditBinding]
    C2 --> CF[SpinBoxBinding]
    
    C3 --> CG[ListViewBinding]
    C3 --> CH[TableViewBinding]
    
    C4 --> CI[DateEditBinding]
    C4 --> CJ[TimeEditBinding]
    C4 --> CK[DateTimeEditBinding]