# core/mod_manager.py
from typing import List, Dict, Any, Tuple
from .file_handler import FileHandler

class ModManager:
    def __init__(self):
        self.file_handler = FileHandler()
        self.mods = []
        self.global_settings = []
        self.original_mods_order = []
        self.current_mod_active_path = ""
        self.current_priority_path = ""
    
    def load_mods(self, mod_active_path: str, priority_path: str) -> Tuple[bool, str]:
        """加载模组数据"""
        try:
            # 验证文件路径
            if not self.file_handler.validate_file_path(mod_active_path):
                return False, f"ModActive文件不存在: {mod_active_path}"
            
            if not self.file_handler.validate_file_path(priority_path):
                return False, f"Priority文件不存在: {priority_path}"
            
            # 读取文件
            mod_active_data = self.file_handler.read_mod_active_file(mod_active_path)
            priority_data = self.file_handler.read_priority_file(priority_path)
            
            # 合并数据
            self.mods, self.global_settings = self.file_handler.merge_mod_data(
                mod_active_data, priority_data
            )
            
            # 保存原始顺序和文件路径
            self.original_mods_order = self.mods.copy()
            self.current_mod_active_path = mod_active_path
            self.current_priority_path = priority_path
            
            message = f"成功加载 {len(self.mods)} 个模组和 {len(self.global_settings)} 个全局设置"
            print(f"✅ {message}")
            return True, message
            
        except Exception as e:
            error_msg = f"加载模组失败: {e}"
            print(f"❌ {error_msg}")
            return False, error_msg
    
    def save_mods(self, mod_active_path: str = None, priority_path: str = None) -> Tuple[bool, str]:
        """保存模组数据"""
        try:
            # 使用当前路径或提供的路径
            save_mod_active_path = mod_active_path or self.current_mod_active_path
            save_priority_path = priority_path or self.current_priority_path
            
            if not save_mod_active_path or not save_priority_path:
                return False, "未设置保存路径"
            
            # 导出数据
            mod_active_data, priority_data = self.file_handler.export_mod_data(
                self.mods, self.global_settings
            )
            
            # 写入文件
            success1 = self.file_handler.write_mod_active_file(mod_active_data, save_mod_active_path)
            success2 = self.file_handler.write_priority_file(priority_data, save_priority_path)
            
            if success1 and success2:
                # 更新原始顺序
                self.original_mods_order = self.mods.copy()
                message = f"成功保存 {len(self.mods)} 个模组"
                print(f"✅ {message}")
                return True, message
            else:
                return False, "保存文件失败"
                
        except Exception as e:
            error_msg = f"保存模组失败: {e}"
            print(f"❌ {error_msg}")
            return False, error_msg
    
    def update_mod_status(self, mod_key: str, enabled: bool) -> bool:
        """更新单个模组状态"""
        for mod in self.mods:
            if mod["key"] == mod_key:
                mod["enabled"] = enabled
                print(f"🔄 更新模组状态: {mod_key} -> {'启用' if enabled else '禁用'}")
                return True
        print(f"⚠️ 未找到模组: {mod_key}")
        return False
    
    def batch_update_mod_status(self, mod_keys: List[str], enabled: bool) -> int:
        """批量更新模组状态"""
        updated_count = 0
        for mod in self.mods:
            if mod["key"] in mod_keys:
                mod["enabled"] = enabled
                updated_count += 1
        
        print(f"🔄 批量更新 {updated_count} 个模组状态 -> {'启用' if enabled else '禁用'}")
        return updated_count
    
    def reorder_mods(self, new_order: List[str]) -> bool:
        """重新排序模组"""
        try:
            # 根据新的键名顺序重新排列模组
            key_to_mod = {mod["key"]: mod for mod in self.mods}
            
            # 验证所有键名都存在
            for key in new_order:
                if key not in key_to_mod:
                    print(f"⚠️ 重新排序时未找到模组: {key}")
                    return False
            
            # 应用新顺序
            self.mods = [key_to_mod[key] for key in new_order if key in key_to_mod]
            
            # 更新优先级数值
            for i, mod in enumerate(self.mods):
                mod["priority"] = i
            
            print(f"🔄 重新排序模组，新顺序: {len(self.mods)} 个模组")
            return True
            
        except Exception as e:
            print(f"❌ 重新排序模组失败: {e}")
            return False
    
    def move_mods_to_top(self, mod_keys: List[str]) -> bool:
        """移动模组到顶部"""
        try:
            # 分离要移动的模组和其他模组
            mods_to_move = [mod for mod in self.mods if mod["key"] in mod_keys]
            other_mods = [mod for mod in self.mods if mod["key"] not in mod_keys]
            
            # 重新组合：移动的模组在前，其他模组在后
            self.mods = mods_to_move + other_mods
            
            # 更新优先级数值
            for i, mod in enumerate(self.mods):
                mod["priority"] = i
            
            print(f"⬆️ 移动 {len(mods_to_move)} 个模组到顶部")
            return True
            
        except Exception as e:
            print(f"❌ 移动模组到顶部失败: {e}")
            return False
    
    def move_mods_to_bottom(self, mod_keys: List[str]) -> bool:
        """移动模组到底部"""
        try:
            # 分离要移动的模组和其他模组
            mods_to_move = [mod for mod in self.mods if mod["key"] in mod_keys]
            other_mods = [mod for mod in self.mods if mod["key"] not in mod_keys]
            
            # 重新组合：其他模组在前，移动的模组在后
            self.mods = other_mods + mods_to_move
            
            # 更新优先级数值
            for i, mod in enumerate(self.mods):
                mod["priority"] = i
            
            print(f"⬇️ 移动 {len(mods_to_move)} 个模组到底部")
            return True
            
        except Exception as e:
            print(f"❌ 移动模组到底部失败: {e}")
            return False
    
    def get_mods(self) -> List[Dict[str, Any]]:
        """获取模组列表"""
        return self.mods
    
    def get_global_settings(self) -> List[Dict[str, Any]]:
        """获取全局设置列表"""
        return self.global_settings
    
    def get_mod_by_key(self, mod_key: str) -> Dict[str, Any]:
        """根据键名获取模组"""
        for mod in self.mods:
            if mod["key"] == mod_key:
                return mod
        return {}
    
    def has_unsaved_changes(self) -> bool:
        """检查是否有未保存的更改"""
        if not self.original_mods_order:
            return False
        
        # 检查顺序是否改变
        if len(self.mods) != len(self.original_mods_order):
            return True
        
        for i, (current, original) in enumerate(zip(self.mods, self.original_mods_order)):
            if current["key"] != original["key"]:
                return True
            if current["enabled"] != original["enabled"]:
                return True
        
        return False
    
    def get_stats(self) -> Dict[str, Any]:
        """获取统计信息"""
        enabled_count = sum(1 for mod in self.mods if mod["enabled"])
        
        return {
            "total_mods": len(self.mods),
            "enabled_mods": enabled_count,
            "disabled_mods": len(self.mods) - enabled_count,
            "global_settings": len(self.global_settings),
            "has_unsaved_changes": self.has_unsaved_changes(),
            "mod_active_file": self.current_mod_active_path,
            "priority_file": self.current_priority_path
        }