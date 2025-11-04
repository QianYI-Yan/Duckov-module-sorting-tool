# ui/webview_app.py
import webview
import os
from pathlib import Path

class ModManagerApp:
    def __init__(self):
        self.window = None
        self.mod_manager = None
        self.event_handler = None
        self.html_content = self._get_loading_html()
    
    def _initialize_managers(self):
        """初始化管理器"""
        try:
            from core.mod_manager import ModManager
            from .event_handler import EventHandler
            
            self.mod_manager = ModManager()
            self.event_handler = EventHandler(self.mod_manager)
            return True
        except Exception as e:
            print(f"❌ 初始化管理器失败: {e}")
            return False
    
    def _get_loading_html(self):
        """获取加载中的HTML页面"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>游戏模组管理器 - 加载中</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    color: white;
                }
                .loading-container {
                    text-align: center;
                    background: rgba(255,255,255,0.1);
                    padding: 40px;
                    border-radius: 15px;
                    backdrop-filter: blur(10px);
                }
                .spinner {
                    border: 4px solid rgba(255,255,255,0.3);
                    border-radius: 50%;
                    border-top: 4px solid white;
                    width: 40px;
                    height: 40px;
                    animation: spin 1s linear infinite;
                    margin: 0 auto 20px;
                }
                @keyframes spin {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }
                h1 {
                    margin: 0 0 10px 0;
                    font-weight: 300;
                }
                p {
                    margin: 0;
                    opacity: 0.8;
                }
            </style>
        </head>
        <body>
            <div class="loading-container">
                <div class="spinner"></div>
                <h1>游戏模组管理器</h1>
                <p>正在初始化应用程序...</p>
            </div>
        </body>
        </html>
        """
    
    def _get_error_html(self, error_message):
        """获取错误页面HTML"""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>错误 - 游戏模组管理器</title>
            <style>
                body {{
                    margin: 0;
                    padding: 40px;
                    background: #f8f9fa;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    color: #333;
                }}
                .error-container {{
                    text-align: center;
                    background: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    max-width: 500px;
                }}
                .error-icon {{
                    font-size: 48px;
                    margin-bottom: 20px;
                }}
                h1 {{
                    color: #e74c3c;
                    margin: 0 0 15px 0;
                }}
                .error-message {{
                    background: #f8d7da;
                    color: #721c24;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 20px 0;
                    text-align: left;
                    font-family: monospace;
                    font-size: 14px;
                }}
                button {{
                    background: #3498db;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 14px;
                }}
                button:hover {{
                    background: #2980b9;
                }}
            </style>
        </head>
        <body>
            <div class="error-container">
                <div class="error-icon">⚠️</div>
                <h1>启动错误</h1>
                <p>应用程序启动时遇到问题：</p>
                <div class="error-message">{error_message}</div>
                <p>请检查控制台输出获取更多信息，然后重启应用程序。</p>
                <button onclick="window.close()">关闭</button>
            </div>
        </body>
        </html>
        """
    
    def run(self):
        """运行应用程序"""
        try:
            # 初始化管理器
            if not self._initialize_managers():
                self.html_content = self._get_error_html("无法初始化核心管理器")
            else:
                # 生成主界面HTML
                from .html_generator import HTMLGenerator
                html_generator = HTMLGenerator()
                self.html_content = html_generator.generate_main_html()
            
        except Exception as e:
            print(f"❌ 界面生成失败: {e}")
            self.html_content = self._get_error_html(str(e))
        
        # 创建主窗口
        self.window = webview.create_window(
            '游戏模组管理器',
            html=self.html_content,
            js_api=self.event_handler,
            width=1200,
            height=800,
            min_size=(800, 600),
            resizable=True,
            background_color='#2c3e50'
        )
        
        print("🖥️  WebView窗口已创建")
        print("📍  应用程序已启动，窗口显示中...")
        
        # 启动WebView
        webview.start(debug=True)