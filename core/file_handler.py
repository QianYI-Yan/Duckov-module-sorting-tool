# core/file_handler.py
import json
import os
from pathlib import Path
from typing import Dict, List, Any, Tuple

class FileHandler:
    def __init__(self):
        pass
    
    def read_mod_active_file(self, file_path: str) -> Dict[str, Any]:
        """读取ModActive文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"✅ 成功读取ModActive文件: {os.path.basename(file_path)}")
                return data
        except Exception as e:
            print(f"❌ 读取ModActive文件失败: {e}")
            return {}
    
    def read_priority_file(self, file_path: str) -> Dict[str, Any]:
        """读取Priority文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"✅ 成功读取Priority文件: {os.path.basename(file_path)}")
                return data
        except Exception as e:
            print(f"❌ 读取Priority文件失败: {e}")
            return {}
    
    def write_mod_active_file(self, data: Dict[str, Any], file_path: str) -> bool:
        """写入ModActive文件"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ 成功写入ModActive文件: {os.path.basename(file_path)}")
            return True
        except Exception as e:
            print(f"❌ 写入ModActive文件失败: {e}")
            return False
    
    def write_priority_file(self, data: Dict[str, Any], file_path: str) -> bool:
        """写入Priority文件"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ 成功写入Priority文件: {os.path.basename(file_path)}")
            return True
        except Exception as e:
            print(f"❌ 写入Priority文件失败: {e}")
            return False
    
    def merge_mod_data(self, mod_active_data: Dict, priority_data: Dict) -> Tuple[List[Dict], List[Dict]]:
        """
        合并两个文件的数据
        
        Returns:
            Tuple: (模组列表, 全局设置列表)
        """
        mods = []
        global_settings = []
        
        # 处理全局设置（非模组条目）
        for key, value in mod_active_data.items():
            if not key.startswith("ModActive_"):
                global_settings.append({
                    "key": key,
                    "value": value,
                    "type": "global_setting"
                })
        
        for key, value in priority_data.items():
            if not key.startswith("priority_") and not any(g["key"] == key for g in global_settings):
                global_settings.append({
                    "key": key,
                    "value": value,
                    "type": "global_setting"
                })
        
        # 收集所有模组键名
        all_mod_keys = set()
        
        # 从ModActive文件中提取模组
        for key in mod_active_data.keys():
            if key.startswith("ModActive_"):
                mod_key = key.replace("ModActive_", "")
                all_mod_keys.add(mod_key)
        
        # 从Priority文件中提取模组
        for key in priority_data.keys():
            if key.startswith("priority_"):
                mod_key = key.replace("priority_", "")
                all_mod_keys.add(mod_key)
        
        # 创建模组数据
        for mod_key in all_mod_keys:
            mod_data = {
                "key": mod_key,
                "friendly_name": mod_key,  # 默认使用原始键名
                "enabled": False,
                "priority": 9999,
                "mod_type": "Unknown",
                "raw_mod_active_key": f"ModActive_{mod_key}",
                "raw_priority_key": f"priority_{mod_key}",
                "web_url": "",
                "is_global": False
            }
            
            # 设置启用状态
            mod_active_key = f"ModActive_{mod_key}"
            if mod_active_key in mod_active_data:
                mod_data["enabled"] = mod_active_data[mod_active_key].get("value", False)
            
            # 设置优先级
            priority_key = f"priority_{mod_key}"
            if priority_key in priority_data:
                mod_data["priority"] = priority_data[priority_key].get("value", 9999)
            
            mods.append(mod_data)
        
        # 按优先级排序
        mods.sort(key=lambda x: x["priority"])
        
        return mods, global_settings
    
    def export_mod_data(self, mods: List[Dict], global_settings: List[Dict]) -> Tuple[Dict, Dict]:
        """
        导出模组数据为两个文件的结构
        
        Returns:
            Tuple: (ModActive数据, Priority数据)
        """
        mod_active_data = {}
        priority_data = {}
        
        # 添加全局设置到ModActive
        for setting in global_settings:
            if setting["type"] == "global_setting":
                mod_active_data[setting["key"]] = setting["value"]
        
        # 构建模组数据
        for i, mod in enumerate(mods):
            # ModActive数据
            mod_active_key = mod["raw_mod_active_key"]
            mod_active_data[mod_active_key] = {
                "__type": "bool",
                "value": mod["enabled"]
            }
            
            # Priority数据（使用当前顺序作为优先级）
            priority_key = mod["raw_priority_key"]
            priority_data[priority_key] = {
                "__type": "int", 
                "value": i
            }
        
        return mod_active_data, priority_data
    
    def validate_file_path(self, file_path: str) -> bool:
        """验证文件路径是否存在且可访问"""
        try:
            path = Path(file_path)
            return path.exists() and path.is_file()
        except Exception:
            return False
    
    def get_file_info(self, file_path: str) -> Dict[str, Any]:
        """获取文件信息"""
        try:
            path = Path(file_path)
            stat = path.stat()
            return {
                "exists": path.exists(),
                "size": stat.st_size if path.exists() else 0,
                "modified_time": stat.st_mtime if path.exists() else 0,
                "is_file": path.is_file() if path.exists() else False
            }
        except Exception as e:
            print(f"获取文件信息失败: {e}")
            return {"exists": False, "size": 0, "modified_time": 0, "is_file": False}