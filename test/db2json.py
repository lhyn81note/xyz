import os
import sqlite3
from sqlalchemy import Column, Integer, Float, String, VARCHAR, DateTime, CHAR

def get_all_tables(db_path):
    # 连接到 SQLite 数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 获取所有表名
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    
    # 关闭连接
    conn.close()
    
    return tables

def get_table_structure(db_path, table_name):
    # 连接到 SQLite 数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 获取表结构
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    
    # 关闭连接
    conn.close()
    
    return columns

def generate_class_code(table_name, columns):
    # 定义类代码模板
    class_template =  f"from models.__base__ import *\n"
    class_template += f"from libs.binding.dtobase import DtoBase\n"
    class_template += f"from libs.binding.observableCollection import ObservableCollection\n"
    class_template += f"\nclass {table_name}(declarative_base()):\n"  # capitalize()
    class_template += f"    __tablename__ = '{table_name}'\n"
    
    # 遍历列信息并生成代码
    for column in columns:
        column_name = column[1]
        column_type = column[2]
        is_primary_key = column[5] == 1
        
        # 映射 SQLite 数据类型到 SQLAlchemy 数据类型
        if column_type.lower() == 'char': sqlalchemy_type = 'String'
        elif column_type.lower() == 'integer': sqlalchemy_type = 'Integer'
        elif column_type.lower() == 'float': sqlalchemy_type = 'Float'
        elif column_type.lower() == 'datetime': sqlalchemy_type = 'DateTime'
        else: sqlalchemy_type = 'String'  # 默认为 String
        
        # 生成列代码
        if is_primary_key:
            class_template += f"    {column_name} = Column({sqlalchemy_type}, primary_key=True)\n"
        else:
            class_template += f"    {column_name} = Column({sqlalchemy_type})\n"
        
    class_template += f"\n    class HandlerBase(ServiceBase):\n"
    class_template += f"        def __init__(self, T, engine):\n"
    class_template += f"            super().__init__(T, engine)\n"

    class_template += f"\n    def __init__(self, engine) -> None:\n"
    class_template += f"        self.Handler = {table_name}.HandlerBase({table_name}, engine)\n"

    class_template += f"\n    def dto(self):\n"
    class_template += f"        dto = DtoBase()\n"
    class_template += f"        for propname in {table_name}.__table__.columns.keys():\n"
    class_template += f"            dto.__setattr__(propname, getattr(self, propname))\n"
    class_template += f"        return dto\n"
    
    return class_template

def save_class_to_file(table_name, class_code):
    # 保存类代码到文件
    file_name = f"{table_name}.py"
    with open(file_name, 'w') as file:
        file.write(class_code)

# 示例用法
db_folder = '..\db'
for db_file in os.listdir(db_folder):
    db_path = os.path.join(db_folder, db_file)
    # print(f"######## 处理数据库:{db_path} #########")
    tables = get_all_tables(db_path)

    for table_name in tables:
        # print(f"处理数据表:{table_name}")
        columns = get_table_structure(db_path, table_name)
        class_code = generate_class_code(table_name, columns)
        save_class_to_file(table_name, class_code)
    # print(f"生成了{len(tables)}个类文件")