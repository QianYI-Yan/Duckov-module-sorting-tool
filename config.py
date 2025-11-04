# config.py
import json
import os
from pathlib import Path

class Config:
    def __init__(self):
        self.config_dir = Path("data")
        self.config_file = self.config_dir / "app_config.json"
        self.default_config = {
            "mod_source_url": "",
            "auto_backup": True,
            "max_history_steps": 400,
            "theme": "dark",
            "language": "zh-CN",
            "recent_files": []
        }
        self.current_config = self.default_config.copy()
        self._ensure_directories()
        self.load_config()
    
    def _ensure_directories(self):
        """确保所需目录存在"""
        directories = [
            self.config_dir,
            self.config_dir / "back",
            self.config_dir / "backup", 
            self.config_dir / "cache",
            Path("lib") / "translations"
        ]
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def load_config(self):
        """加载配置文件"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                    self.current_config.update(loaded_config)
        except Exception as e:
            print(f"加载配置失败: {e}")
    
    def save_config(self):
        """保存配置文件"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.current_config, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"保存配置失败: {e}")
            return False
    
    def get(self, key, default=None):
        return self.current_config.get(key, default)
    
    def set(self, key, value):
        self.current_config[key] = value
        return self.save_config()
    
    def add_recent_file(self, file_path, file_type):
        """添加最近使用的文件"""
        recent_entry = {
            "path": file_path,
            "type": file_type,
            "name": os.path.basename(file_path)
        }
        
        # 移除重复项
        self.current_config["recent_files"] = [
            f for f in self.current_config["recent_files"] 
            if f["path"] != file_path
        ]
        
        # 添加到开头
        self.current_config["recent_files"].insert(0, recent_entry)
        
        # 只保留最近10个文件
        self.current_config["recent_files"] = self.current_config["recent_files"][:10]
        
        return self.save_config()

# 全局配置实例
app_config = Config()