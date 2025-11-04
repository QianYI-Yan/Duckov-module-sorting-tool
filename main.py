"""
模组管理器主程序入口
游戏模组加载顺序编辑器 - 基于Python和WebView2
"""

import sys
import os
import traceback
from pathlib import Path

# 添加项目根目录到Python路径，确保模块导入正常工作
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def setup_environment():
    """设置运行环境"""
    try:
        # 确保必要的目录存在
        required_dirs = [
            'data/back',
            'data/backup', 
            'data/cache',
            'lib/translations',
            'resources'
        ]
        
        for dir_path in required_dirs:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
            
        print("✅ 环境检查完成")
        return True
        
    except Exception as e:
        print(f"❌ 环境设置失败: {e}")
        return False

def check_dependencies():
    """检查必要的依赖是否安装"""
    try:
        import webview
        import requests
        import send2trash
        print("✅ 所有依赖已安装")
        return True
    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        print("请运行: pip install -r requirements.txt")
        return False

def main():
    """应用程序主函数"""
    print("=" * 50)
    print("🎮 游戏模组管理器 - 启动中...")
    print("=" * 50)
    
    try:
        # 1. 设置环境
        if not setup_environment():
            input("按回车键退出...")
            return
        
        # 2. 检查依赖
        if not check_dependencies():
            input("按回车键退出...")
            return
        
        # 3. 导入核心模块
        print("📦 加载核心模块...")
        from config import app_config
        from ui.webview_app import ModManagerApp
        
        # 4. 创建并运行应用
        print("🚀 启动用户界面...")
        app = ModManagerApp()
        app.run()
        
    except Exception as e:
        print(f"❌ 应用程序启动失败: {e}")
        print("\n详细错误信息:")
        traceback.print_exc()
        print("\n可能的原因:")
        print("1. 缺少必要的依赖包")
        print("2. 模块导入路径问题") 
        print("3. 系统兼容性问题")
        print("\n请确保:")
        print("- 已安装 requirements.txt 中的所有依赖")
        print("- 在项目根目录运行此脚本")
        print("- 系统已安装 WebView2 Runtime")
        
        input("\n按回车键退出...")

if __name__ == "__main__":
    main()