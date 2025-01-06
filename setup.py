from cx_Freeze import setup, Executable
import os

# 设置包含的额外文件
includefiles = [
    ('static', 'static'),  # (source, destination) 形式
    ('templates', 'templates')  # (source, destination) 形式
]

# 设置选项
options = {
    'build_exe': {
        'packages': ['uvicorn'],
        'excludes': [],
        'include_files': includefiles
    }
}

# 设置执行文件
executables = [
    Executable('main.py', base=None)
]

# 运行打包
setup(
    name="MyApp",
    version="0.1",
    description="My application",
    options=options,
    executables=executables
)