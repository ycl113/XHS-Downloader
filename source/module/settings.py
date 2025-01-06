from json import dump
from json import load
from pathlib import Path
from platform import system

from .static import ROOT
from .static import USERAGENT

__all__ = ['Settings']

class Settings:
    # 默认设置
    default = {
        "work_path": "",
        "folder_name": "Download",
        "name_format": "发布时间 作者昵称 作品标题",
        "user_agent": USERAGENT,
        "cookie": "",
        "proxy": None,
        "timeout": 10,
        "chunk": 1024 * 1024 * 2,
        "max_retry": 5,
        "record_data": False,
        "image_format": "PNG",
        "image_download": True,
        "video_download": True,
        "live_download": False,
        "folder_mode": False,
        "download_record": True,
        "language": "zh_CN",
    }
    # 根据操作系统设置编码格式
    encode = "UTF-8-SIG" if system() == "Windows" else "UTF-8"

    def __init__(self, root: Path = ROOT):
        # 初始化设置文件路径
        self.file = root.joinpath("./settings.json")

    def run(self):
        # 如果设置文件存在，读取文件，否则创建文件
        return self.read() if self.file.is_file() else self.create()

    def read(self) -> dict:
        # 读取设置文件并返回内容
        with self.file.open("r", encoding=self.encode) as f:
            return load(f)

    def create(self) -> dict:
        # 创建设置文件并写入默认设置
        with self.file.open("w", encoding=self.encode) as f:
            dump(self.default, f, indent=4, ensure_ascii=False)
            return self.default

    def update(self, data: dict):
        # 更新设置文件内容
        with self.file.open("w", encoding=self.encode) as f:
            dump(data, f, indent=4, ensure_ascii=False)

    @classmethod
    def check_keys(
            cls,
            data: dict,
            callback: callable,
            *args,
            **kwargs,
    ) -> dict:
        # 检查给定的数据字典是否包含所有必需的键
        needful_keys = set(cls.default.keys())
        given_keys = set(data.keys())
        if not needful_keys.issubset(given_keys):
            # 如果缺少必需的键，调用回调函数并返回默认设置
            callback(*args, **kwargs)
            return cls.default
        # 如果所有必需的键都存在，返回给定的数据
        return data