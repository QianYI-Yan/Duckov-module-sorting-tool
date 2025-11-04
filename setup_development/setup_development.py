"""
开发环境初始化脚本
"""
import os
import subprocess
import sys
from pathlib import Path

def setup_development_environment():
    """设置完整的开发环境"""
    
    print("🚀 正在设置模组管理器开发环境...")
    
    # 创建目录结构
    directories = [
        'core',
        'ui', 
        'utils',
        'data/back',
        'data/backup',
        'data/cache',
        'lib/translations',
        'resources',
        'tests',
        '.vscode'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 创建目录: {directory}")
    
    # 创建基础文件
    base_files = {
        'requirements.txt': """pywebview>=3.6
requests>=2.25.0
send2trash>=1.8.0
pathlib2>=2.3.0; python_version < '3.4'""",
        
        'README.md': """# 游戏模组管理器

一个功能强大的游戏模组加载顺序管理工具。

## 开发环境设置

1. 创建虚拟环境: `python -m venv venv`
2. 激活虚拟环境: `venv\\Scripts\\activate` (Windows)
3. 安装依赖: `pip install -r requirements.txt`
4. 运行: `python main.py`

## 项目结构
参考项目文档。""",
        
        '.gitignore': """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Data files (don't version control user data)
data/back/
data/backup/
data/cache/

# Build artifacts
packaging_setup.py
build.bat
build.sh
dist/
""",
        
        'main.py': '''"""
模组管理器主程序入口
"""
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.webview_app import ModManagerApp

def main():
    """应用程序主函数"""
    print("🎮 启动模组管理器...")
    app = ModManagerApp()
    app.run()

if __name__ == "__main__":
    main()'''
    }
    
    for filename, content in base_files.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"📄 创建文件: {filename}")
    
    print("✅ 开发环境设置完成！")
    print("\n下一步:")
    print("1. 在VSCode中打开本项目")
    print("2. 选择虚拟环境解释器 (Ctrl+Shift+P -> 'Python: Select Interpreter')")
    print("3. 开始编写代码!")

if __name__ == "__main__":
    setup_development_environment()