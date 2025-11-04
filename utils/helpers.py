"""
通用辅助函数
"""
import os
import re
from typing import Dict, List, Any
from pathlib import Path

def extract_mod_key(raw_key: str) -> str:
    """从原始键名提取模组ID"""
    if raw_key.startswith("ModActive_"):
        return raw_key.replace("ModActive_", "")
    elif raw_key.startswith("priority_"):
        return raw_key.replace("priority_", "")
    return raw_key

def is_mod_key(key: str) -> bool:
    """检查是否是模组键名"""
    return key.startswith("ModActive_") or key.startswith("priority_")

def is_global_setting(key: str) -> bool:
    """检查是否是全局设置"""
    return not is_mod_key(key)

def sanitize_filename(name: str) -> str:
    """清理文件名，移除非法字符"""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def get_file_size(file_path: str) -> int:
    """获取文件大小（字节）"""
    try:
        return os.path.getsize(file_path)
    except:
        return 0

def ensure_directory(directory: str) -> bool:
    """确保目录存在"""
    try:
        Path(directory).mkdir(parents=True, exist_ok=True)
        return True
    except:
        return False