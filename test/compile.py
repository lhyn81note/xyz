import py_compile
import os
import shutil
from pathlib import Path

def compile_package(src_dir, dst_dir):
    """
    编译整个包到pyc文件
    src_dir: 源代码目录
    dst_dir: 编译后的目标目录
    """
    # 确保目标目录存在
    os.makedirs(dst_dir, exist_ok=True)
    
    # 遍历源目录
    for root, dirs, files in os.walk(src_dir):
        # 计算相对路径
        rel_path = os.path.relpath(root, src_dir)
        # 创建目标子目录
        dst_path = os.path.join(dst_dir, rel_path)
        os.makedirs(dst_path, exist_ok=True)
        
        # 编译每个.py文件
        for file in files:
            if file.endswith('.py') and not file.startswith('_view'):
                src_file = os.path.join(root, file)
                # pyc文件将被放在 __pycache__ 目录下
                py_compile.compile(src_file, 
                                 cfile=os.path.join(dst_path, file + 'c'),
                                 optimize=2)
                
        # 复制__init__.py (如果存在)
        init_py = os.path.join(root, '__init__.py')
        if os.path.exists(init_py):
            py_compile.compile(init_py,
                             cfile=os.path.join(dst_path, '__init__.pyc'),
                             optimize=2)

if __name__ == '__main__':
    
    # 执行编译
    compile_package('../view', './pyc/view')
    compile_package('../wgts', './pyc/wgts')