# ui/event_handler.py
import os
from typing import Dict, List, Any

class EventHandler:
    def __init__(self, mod_manager):
        self.mod_manager = mod_manager
    
    def handle_file_load(self, mod_active_path: str, priority_path: str) -> Dict[str, Any]:
        """处理文件加载事件"""
        try:
            success, message = self.mod_manager.load_mods(mod_active_path, priority_path)
            
            if success:
                mods = self.mod_manager.get_mods()
                global_settings = self.mod_manager.get_global_settings()
                stats = self.mod_manager.get_stats()
                
                return {
                    "success": True,
                    "message": message,
                    "mods": mods,
                    "global_settings": global_settings,
                    "stats": stats
                }
            else:
                return {
                    "success": False,
                    "message": message
                }
                
        except Exception as e:
            return {
                "success": False,
                "message": f"加载文件时发生错误: {str(e)}"
            }
    
    def handle_file_save(self, mod_active_path: str = None, priority_path: str = None) -> Dict[str, Any]:
        """处理文件保存事件"""
        try:
            success, message = self.mod_manager.save_mods(mod_active_path, priority_path)
            
            if success:
                stats = self.mod_manager.get_stats()
                return {
                    "success": True,
                    "message": message,
                    "stats": stats
                }
            else:
                return {
                    "success": False,
                    "message": message
                }
                
        except Exception as e:
            return {
                "success": False,
                "message": f"保存文件时发生错误: {str(e)}"
            }
    
    def handle_mod_toggle(self, mod_key: str, enabled: bool) -> Dict[str, Any]:
        """处理模组切换事件"""
        try:
            success = self.mod_manager.update_mod_status(mod_key, enabled)
            
            if success:
                stats = self.mod_manager.get_stats()
                return {
                    "success": True,
                    "message": f"模组 {mod_key} 已{'启用' if enabled else '禁用'}",
                    "stats": stats
                }
            else:
                return {
                    "success": False,
                    "message": f"找不到模组: {mod_key}"
                }
                
        except Exception as e:
            return {
                "success": False,
                "message": f"切换模组状态时发生错误: {str(e)}"
            }
    
    def handle_batch_toggle(self, mod_keys: List[str], enabled: bool) -> Dict[str, Any]:
        """处理批量切换事件"""
        try:
            updated_count = self.mod_manager.batch_update_mod_status(mod_keys, enabled)
            
            stats = self.mod_manager.get_stats()
            return {
                "success": True,
                "message": f"已{'启用' if enabled else '禁用'} {updated_count} 个模组",
                "stats": stats
            }
                
        except Exception as e:
            return {
                "success": False,
                "message": f"批量操作时发生错误: {str(e)}"
            }

    
    def handle_mod_reorder(self, new_order: List[str]) -> Dict[str, Any]:
        """处理模组重新排序事件"""
        try:
            success = self.mod_manager.reorder_mods(new_order)
            
            if success:
                stats = self.mod_manager.get_stats()
                return {
                    "success": True,
                    "message": f"已重新排序 {len(new_order)} 个模组",
                    "stats": stats
                }
            else:
                return {
                    "success": False,
                    "message": "重新排序失败"
                }
                
        except Exception as e:
            return {
                "success": False,
                "message": f"重新排序时发生错误: {str(e)}"
            }
    
    def handle_move_to_top(self, mod_keys: List[str]) -> Dict[str, Any]:
        """处理移动到顶部事件"""
        try:
            success = self.mod_manager.move_mods_to_top(mod_keys)
            
            if success:
                stats = self.mod_manager.get_stats()
                return {
                    "success": True,
                    "message": f"已将 {len(mod_keys)} 个模组移动到顶部",
                    "stats": stats
                }
            else:
                return {
                    "success": False,
                    "message": "移动到顶部失败"
                }
                
        except Exception as e:
            return {
                "success": False,
                "message": f"移动到顶部时发生错误: {str(e)}"
            }

    def handle_move_to_bottom(self, mod_keys: List[str]) -> Dict[str, Any]:
        """移动模组到底部"""
        try:
            success = self.mod_manager.move_mods_to_bottom(mod_keys)
            
            if success:
                stats = self.mod_manager.get_stats()
                return {
                    "success": True,
                    "message": f"已将 {len(mod_keys)} 个模组移动到底部",
                    "stats": stats
                }
            else:
                return {
                    "success": False,
                    "message": "移动到底部失败"
                }
                
        except Exception as e:
            return {
                "success": False,
                "message": f"移动到底部时发生错误: {str(e)}"
            }
    
    def get_current_state(self) -> Dict[str, Any]:
        """获取当前状态"""
        try:
            mods = self.mod_manager.get_mods()
            global_settings = self.mod_manager.get_global_settings()
            stats = self.mod_manager.get_stats()
            
            return {
                "success": True,
                "mods": mods,
                "global_settings": global_settings,
                "stats": stats
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"获取状态时发生错误: {str(e)}"
            }
        
    def check_file_exists(self, file_path: str) -> Dict[str, Any]:
        """检查文件是否存在"""
        try:
            exists = os.path.exists(file_path)
            return {
                "success": True,
                "exists": exists,
                "path": file_path
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"检查文件存在性时发生错误: {str(e)}"
            }

    def handle_file_load_data(self, mod_active_data: Dict, priority_data: Dict) -> Dict[str, Any]:
        """通过文件数据加载模组（而不是文件路径）"""
        try:
            # 使用文件管理器合并数据
            from core.file_handler import FileHandler
            file_handler = FileHandler()
            
            mods, global_settings = file_handler.merge_mod_data(mod_active_data, priority_data)
            
            # 更新模组管理器状态
            self.mod_manager.mods = mods
            self.mod_manager.global_settings = global_settings
            self.mod_manager.original_mods_order = mods.copy()
            
            stats = self.mod_manager.get_stats()
            
            return {
                "success": True,
                "message": f"成功加载 {len(mods)} 个模组和 {len(global_settings)} 个全局设置",
                "mods": mods,
                "global_settings": global_settings,
                "stats": stats
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"加载模组数据失败: {str(e)}"
            }

    def handle_file_save_data(self) -> Dict[str, Any]:
        """保存模组数据（返回数据而不是保存到文件）"""
        try:
            # 导出数据
            mod_active_data, priority_data = self.mod_manager.file_handler.export_mod_data(
                self.mod_manager.mods, self.mod_manager.global_settings
            )
            
            stats = self.mod_manager.get_stats()
            return {
                "success": True,
                "message": f"成功导出 {len(self.mod_manager.mods)} 个模组数据",
                "mod_active_data": mod_active_data,
                "priority_data": priority_data,
                "stats": stats
            }
                
        except Exception as e:
            return {
                "success": False,
                "message": f"导出模组数据失败: {str(e)}"
            }

    def get_test_files(self) -> Dict[str, Any]:
        """获取测试文件数据"""
        try:
            test_mod_active_path = "test_mod_active.json"
            test_priority_path = "test_priority.json"
            
            # 检查测试文件是否存在
            if not os.path.exists(test_mod_active_path) or not os.path.exists(test_priority_path):
                return {
                    "success": True,
                    "has_test_files": False,
                    "message": "未找到测试文件"
                }
            
            # 读取测试文件
            mod_active_data = self.mod_manager.file_handler.read_mod_active_file(test_mod_active_path)
            priority_data = self.mod_manager.file_handler.read_priority_file(test_priority_path)
            
            return {
                "success": True,
                "has_test_files": True,
                "mod_active_data": mod_active_data,
                "priority_data": priority_data,
                "message": "找到测试文件"
            }
            
        except Exception as e:
            return {
                "success": False,
                "has_test_files": False,
                "message": f"检查测试文件时发生错误: {str(e)}"
            }