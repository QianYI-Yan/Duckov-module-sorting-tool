# ui/html_generator.py
import os
from pathlib import Path

class HTMLGenerator:
    def __init__(self):
        pass

    def generate_main_html(self):
        """生成主界面HTML"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>游戏模组管理器</title>
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: #333;
                    min-height: 100vh;
                }
                
                .container {
                    max-width: 1400px;
                    margin: 0 auto;
                    background: white;
                    min-height: 100vh;
                    box-shadow: 0 0 20px rgba(0,0,0,0.1);
                    display: flex;
                    flex-direction: column;
                }
                
                header {
                    background: #2c3e50;
                    color: white;
                    padding: 25px 30px;
                }
                
                h1 {
                    font-size: 28px;
                    margin-bottom: 8px;
                    font-weight: 600;
                }
                
                .subtitle {
                    opacity: 0.8;
                    font-size: 16px;
                }
                
                .controls {
                    padding: 20px 30px;
                    background: #f8f9fa;
                    border-bottom: 1px solid #dee2e6;
                    display: flex;
                    gap: 12px;
                    flex-wrap: wrap;
                    align-items: center;
                }
                
                button {
                    padding: 10px 18px;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                    font-weight: 600;
                    font-size: 14px;
                    transition: all 0.2s ease;
                    display: flex;
                    align-items: center;
                    gap: 6px;
                }
                
                .btn-primary {
                    background: #3498db;
                    color: white;
                }
                
                .btn-success {
                    background: #27ae60;
                    color: white;
                }
                
                .btn-danger {
                    background: #e74c3c;
                    color: white;
                }
                
                .btn-secondary {
                    background: #95a5a6;
                    color: white;
                }
                
                button:hover:not(:disabled) {
                    transform: translateY(-1px);
                    box-shadow: 0 3px 6px rgba(0,0,0,0.15);
                }
                
                button:disabled {
                    opacity: 0.6;
                    cursor: not-allowed;
                    transform: none !important;
                }
                
                .file-input {
                    display: none;
                }
                
                .file-info {
                    margin-left: auto;
                    display: flex;
                    gap: 20px;
                    font-size: 14px;
                    color: #6c757d;
                }
                
                .file-item {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                }
                
                .main-content {
                    flex: 1;
                    display: flex;
                    overflow: hidden;
                }
                
                .welcome-section {
                    flex: 1;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    padding: 60px 20px;
                    background: #f8f9fa;
                }
                
                .mod-management-section {
                    flex: 1;
                    display: none;
                    flex-direction: column;
                    overflow: hidden;
                }
                
                .mod-list-container {
                    flex: 1;
                    overflow-y: auto;
                    padding: 0;
                }
                
                .mod-list-header {
                    display: grid;
                    grid-template-columns: 50px 1fr 100px 120px 150px;
                    gap: 15px;
                    padding: 15px 20px;
                    background: #34495e;
                    color: white;
                    font-weight: 600;
                    position: sticky;
                    top: 0;
                    z-index: 10;
                }
                
                .mod-item {
                    display: grid;
                    grid-template-columns: 50px 1fr 100px 120px 150px;
                    gap: 15px;
                    padding: 12px 20px;
                    border-bottom: 1px solid #ecf0f1;
                    align-items: center;
                    transition: all 0.2s ease;
                    cursor: move;
                    user-select: none;
                }

                .mod-item.dragging {
                    opacity: 0.5;
                    background: #e3f2fd !important;
                    border: 2px dashed #2196f3;
                }
                
                .mod-item.drag-over {
                    border-top: 3px solid #2196f3;
                    background: #f3f8ff;
                }
                
                .mod-item.selected {
                    background: #e3f2fd !important;
                    border-left: 4px solid #2196f3;
                }
                
                .mod-item.multi-select-area {
                    background: #bbdefb !important;
                }

                .drag-handle {
                    cursor: grab;
                    color: #7f8c8d;
                    font-size: 16px;
                    text-align: center;
                }
                
                .drag-handle:active {
                    cursor: grabbing;
                }
                
                .selection-rectangle {
                    position: absolute;
                    background: rgba(33, 150, 243, 0.2);
                    border: 2px solid #2196f3;
                    pointer-events: none;
                    z-index: 1000;
                }

                .mod-item:hover {
                    background: #f8f9fa;
                }
                
                .mod-item.enabled {
                    background: #d4edda;
                }
                
                .mod-item.disabled {
                    background: #f8d7da;
                    opacity: 0.7;
                }
                
                .mod-checkbox {
                    width: 18px;
                    height: 18px;
                    cursor: pointer;
                }
                
                .mod-name {
                    font-weight: 500;
                }
                
                .mod-id {
                    font-family: monospace;
                    font-size: 12px;
                    color: #6c757d;
                    margin-top: 2px;
                }
                
                .mod-priority {
                    text-align: center;
                    font-family: monospace;
                    background: #e9ecef;
                    padding: 4px 8px;
                    border-radius: 4px;
                    font-weight: bold;
                }
                
                .mod-type {
                    text-align: center;
                    background: #e9ecef;
                    padding: 4px 8px;
                    border-radius: 4px;
                    font-size: 12px;
                    text-transform: uppercase;
                }
                
                .mod-url a {
                    color: #3498db;
                    text-decoration: none;
                }
                
                .mod-url a:hover {
                    text-decoration: underline;
                }
                
                .status-bar {
                    background: #34495e;
                    color: white;
                    padding: 10px 30px;
                    font-size: 14px;
                    display: flex;
                    justify-content: space-between;
                }
                
                .status-message {
                    padding: 15px 30px;
                    margin: 0;
                    display: none;
                }
                
                .status-success {
                    background: #d4edda;
                    color: #155724;
                    border: 1px solid #c3e6cb;
                }
                
                .status-error {
                    background: #f8d7da;
                    color: #721c24;
                    border: 1px solid #f5c6cb;
                }
                
                .status-info {
                    background: #cce7ff;
                    color: #004085;
                    border: 1px solid #b3d7ff;
                }
                
                .empty-state {
                    text-align: center;
                    padding: 60px 20px;
                    color: #7f8c8d;
                }
                
                .empty-state-icon {
                    font-size: 48px;
                    margin-bottom: 16px;
                    opacity: 0.5;
                }
                
                .stats-display {
                    display: flex;
                    gap: 20px;
                    padding: 15px 30px;
                    background: #e9ecef;
                    border-bottom: 1px solid #dee2e6;
                }
                
                .stat-item {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
                
                .stat-value {
                    font-size: 18px;
                    font-weight: bold;
                    color: #2c3e50;
                }
                
                .stat-label {
                    font-size: 12px;
                    color: #7f8c8d;
                    margin-top: 4px;
                }
                
                .file-loading {
                    display: none;
                    align-items: center;
                    gap: 10px;
                    color: #6c757d;
                }
                
                .loading-spinner {
                    width: 16px;
                    height: 16px;
                    border: 2px solid #f3f3f3;
                    border-top: 2px solid #3498db;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;
                }
                
                @keyframes spin {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }

                /* 多选操作栏 */
                .multi-select-toolbar {
                    display: none;
                    padding: 10px 30px;
                    background: #2196f3;
                    color: white;
                    align-items: center;
                    gap: 15px;
                }
                
                .multi-select-toolbar.show {
                    display: flex;
                }
                
                .multi-select-count {
                    font-weight: bold;
                    margin-right: auto;
                }
                
                .multi-select-btn {
                    background: rgba(255,255,255,0.2);
                    border: none;
                    color: white;
                    padding: 6px 12px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 12px;
                }
                
                .multi-select-btn:hover {
                    background: rgba(255,255,255,0.3);
                }
                
                .context-menu {
                    position: fixed;
                    background: white;
                    border: 1px solid #ddd;
                    border-radius: 6px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                    z-index: 10000;
                    min-width: 180px;
                    display: none;
                }

                .context-menu-item {
                    padding: 10px 16px;
                    cursor: pointer;
                    border-bottom: 1px solid #f0f0f0;
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    font-size: 14px;
                }

                .context-menu-item:hover {
                    background: #f5f5f5;
                }

                .context-menu-item:last-child {
                    border-bottom: none;
                }

                .context-menu-divider {
                    height: 1px;
                    background: #f0f0f0;
                    margin: 4px 0;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <header>
                    <h1>🎮 游戏模组管理器</h1>
                    <div class="subtitle">专业的模组加载顺序编辑工具</div>
                </header>
                
                <div class="controls">
                    <button class="btn-primary" onclick="document.getElementById('modActiveFile').click()">
                        📁 加载ModActive文件
                    </button>
                    <button class="btn-primary" onclick="document.getElementById('priorityFile').click()">
                        🔢 加载Priority文件
                    </button>
                    <button class="btn-success" id="saveBtn" disabled onclick="saveModFiles()">
                        💾 保存更改
                    </button>
                    <button class="btn-secondary" id="reorderBtn" disabled onclick="reorderMods()">
                        🔄 重新排序
                    </button>
                    
                    <div class="file-info">
                        <div class="file-item">
                            <span>ModActive:</span>
                            <span id="modActiveFileInfo">未选择</span>
                        </div>
                        <div class="file-item">
                            <span>Priority:</span>
                            <span id="priorityFileInfo">未选择</span>
                        </div>
                    </div>
                </div>
                
                <div class="multi-select-toolbar" id="multiSelectToolbar">
                    <div class="multi-select-count" id="multiSelectCount">已选择 0 个模组</div>
                    <button class="multi-select-btn" onclick="enableSelectedMods()">✅ 启用选中</button>
                    <button class="multi-select-btn" onclick="disableSelectedMods()">❌ 禁用选中</button>
                    <button class="multi-select-btn" onclick="moveSelectedToTop()">⬆️ 移到顶部</button>
                    <button class="multi-select-btn" onclick="moveSelectedToBottom()">⬇️ 移到底部</button>
                    <button class="multi-select-btn" onclick="clearSelection()">✖️ 清除选择</button>
                </div>

                <!-- 隐藏的文件输入 -->
                <input type="file" id="modActiveFile" class="file-input" accept=".json" 
                       onchange="handleModActiveFileSelect(this.files)">
                <input type="file" id="priorityFile" class="file-input" accept=".json" 
                       onchange="handlePriorityFileSelect(this.files)">
                
                <div id="statusMessage" class="status-message"></div>
                
                <div class="file-loading" id="fileLoading">
                    <div class="loading-spinner"></div>
                    <span>正在加载文件...</span>
                </div>
                
                <div class="stats-display" id="statsDisplay" style="display: none;">
                    <div class="stat-item">
                        <div class="stat-value" id="statTotalMods">0</div>
                        <div class="stat-label">总模组</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value" id="statEnabledMods">0</div>
                        <div class="stat-label">已启用</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value" id="statDisabledMods">0</div>
                        <div class="stat-label">已禁用</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-value" id="statUnsavedChanges">0</div>
                        <div class="stat-label">未保存更改</div>
                    </div>
                </div>
                
                <div class="main-content">
                    <div class="welcome-section" id="welcomeSection">
                        <div style="font-size: 64px; margin-bottom: 20px;">🎮</div>
                        <h2 style="font-size: 24px; color: #2c3e50; margin-bottom: 10px;">欢迎使用游戏模组管理器</h2>
                        <p style="color: #7f8c8d; margin-bottom: 25px; line-height: 1.6; max-width: 600px;">
                            这是一个功能强大的模组加载顺序编辑工具，支持拖拽排序、批量操作、完整的历史记录和备份系统。
                        </p>
                        <button class="btn-primary" onclick="document.getElementById('modActiveFile').click()">
                            📁 开始使用 - 加载模组文件
                        </button>
                        
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 30px; max-width: 800px;">
                            <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center;">
                                <div style="font-size: 32px; margin-bottom: 10px;">🔄</div>
                                <h3>智能排序</h3>
                                <p>基于模组源信息的智能加载顺序</p>
                            </div>
                            <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center;">
                                <div style="font-size: 32px; margin-bottom: 10px;">📝</div>
                                <h3>操作历史</h3>
                                <p>完整的操作记录和撤销重做</p>
                            </div>
                            <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center;">
                                <div style="font-size: 32px; margin-bottom: 10px;">💾</div>
                                <h3>备份管理</h3>
                                <p>安全的备份和恢复系统</p>
                            </div>
                            <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center;">
                                <div style="font-size: 32px; margin-bottom: 10px;">🖱️</div>
                                <h3>直观操作</h3>
                                <p>Windows资源管理器式交互</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mod-management-section" id="modManagementSection">
                        <div class="mod-list-container">
                            <div class="mod-list-header">
                                <div>启用</div>
                                <div>模组名称</div>
                                <div>优先级</div>
                                <div>类型</div>
                                <div>Web URL</div>
                            </div>
                            <div id="modList"></div>
                        </div>
                    </div>
                </div>
                
                <div class="status-bar">
                    <div id="statusLeft">就绪</div>
                    <div id="statusRight">v1.0.0</div>
                </div>
            </div>

            <div id="contextMenu" class="context-menu">
                <div class="context-menu-item" onclick="contextMenuEnable()">
                    <span>✅</span> 启用选中
                </div>
                <div class="context-menu-item" onclick="contextMenuDisable()">
                    <span>❌</span> 禁用选中
                </div>
                <div class="context-menu-divider"></div>
                <div class="context-menu-item" onclick="contextMenuMoveToTop()">
                    <span>⬆️</span> 移动到顶部
                </div>
                <div class="context-menu-item" onclick="contextMenuMoveToBottom()">
                    <span>⬇️</span> 移动到底部
                </div>
            </div>

            <script>
                let currentMods = [];
                let selectedMods = new Set();
                let currentModActivePath = '';
                let currentPriorityPath = '';
                let currentModActiveData = null;
                let currentPriorityData = null;
                let currentModActiveFileName = '';
                let currentPriorityFileName = '';
                let isDragging = false;
                let dragStartX = 0;
                let dragStartY = 0;
                let selectionRectangle = null;
                let isMultiSelecting = false;
                
                function showStatus(message, type = 'info') {
                    const statusDiv = document.getElementById('statusMessage');
                    const className = type === 'success' ? 'status-success' : 
                                     type === 'error' ? 'status-error' : 'status-info';
                    
                    statusDiv.innerHTML = `<div class="${className}">${message}</div>`;
                    statusDiv.style.display = 'block';
                    
                    if (type === 'success' || type === 'info') {
                        setTimeout(() => {
                            statusDiv.style.display = 'none';
                        }, 5000);
                    }
                }
                
                function showLoading(show) {
                    document.getElementById('fileLoading').style.display = show ? 'flex' : 'none';
                }
                
                function updateStatusBar(message) {
                    document.getElementById('statusLeft').textContent = message;
                }
                
                function handleModActiveFileSelect(files) {
                    if (files.length === 0) return;
                    
                    const file = files[0];
                    // 使用文件对象而不是路径，因为WebView2可能不支持file.path
                    readFileContent(file).then(content => {
                        try {
                            const data = JSON.parse(content);
                            // 将文件内容传递给后端处理
                            processModActiveFile(data, file.name);
                        } catch (e) {
                            showStatus('ModActive文件格式错误: ' + e.message, 'error');
                        }
                    }).catch(error => {
                        showStatus('读取ModActive文件失败: ' + error, 'error');
                    });
                }

                function handlePriorityFileSelect(files) {
                    if (files.length === 0) return;
                    
                    const file = files[0];
                    readFileContent(file).then(content => {
                        try {
                            const data = JSON.parse(content);
                            // 将文件内容传递给后端处理
                            processPriorityFile(data, file.name);
                        } catch (e) {
                            showStatus('Priority文件格式错误: ' + e.message, 'error');
                        }
                    }).catch(error => {
                        showStatus('读取Priority文件失败: ' + error, 'error');
                    });
                }

                function readFileContent(file) {
                    return new Promise((resolve, reject) => {
                        const reader = new FileReader();
                        reader.onload = function(e) {
                            resolve(e.target.result);
                        };
                        reader.onerror = function(e) {
                            reject(new Error('文件读取失败'));
                        };
                        reader.readAsText(file);
                    });
                }

                function processModActiveFile(data, fileName) {
                    currentModActiveData = data;
                    currentModActiveFileName = fileName;
                    document.getElementById('modActiveFileInfo').textContent = fileName;
                    updateStatusBar(`已选择ModActive文件: ${fileName}`);
                    
                    // 如果两个文件都已选择，自动加载
                    if (currentModActiveData && currentPriorityData) {
                        loadModFiles();
                    }
                }

                function processPriorityFile(data, fileName) {
                    currentPriorityData = data;
                    currentPriorityFileName = fileName;
                    document.getElementById('priorityFileInfo').textContent = fileName;
                    updateStatusBar(`已选择Priority文件: ${fileName}`);
                    
                    // 如果两个文件都已选择，自动加载
                    if (currentModActiveData && currentPriorityData) {
                        loadModFiles();
                    }
                }

                function loadModFiles() {
                    if (!currentModActiveData || !currentPriorityData) {
                        showStatus('请先选择两个文件', 'error');
                        return;
                    }
                    
                    showLoading(true);
                    showStatus('正在加载模组文件...', 'info');
                    updateStatusBar('加载文件中...');
                    
                    // 传递文件数据而不是文件路径
                    pywebview.api.handle_file_load_data(currentModActiveData, currentPriorityData).then(response => {
                        showLoading(false);
                        if (response.success) {
                            currentMods = response.mods;
                            showStatus(response.message, 'success');
                            updateStatusBar('文件加载成功');
                            showModManagement();
                            updateStats(response.stats);
                            renderModList();
                            document.getElementById('saveBtn').disabled = false;
                            document.getElementById('reorderBtn').disabled = false;
                        } else {
                            showStatus(response.message, 'error');
                            updateStatusBar('加载失败');
                        }
                    }).catch(error => {
                        showLoading(false);
                        showStatus('加载文件时发生错误: ' + error, 'error');
                        updateStatusBar('加载错误');
                    });
                }
                
                function saveModFiles() {
                    showStatus('正在保存模组文件...', 'info');
                    updateStatusBar('保存文件中...');
                    
                    pywebview.api.handle_file_save_data().then(response => {
                        if (response.success) {
                            // 创建下载链接
                            downloadJSONFile(response.mod_active_data, 'ModActive.json');
                            downloadJSONFile(response.priority_data, 'Priority.json');
                            
                            showStatus('模组数据已导出为JSON文件', 'success');
                            updateStatusBar('导出成功');
                            updateStats(response.stats);
                        } else {
                            showStatus(response.message, 'error');
                            updateStatusBar('保存失败');
                        }
                    }).catch(error => {
                        showStatus('保存文件时发生错误: ' + error, 'error');
                        updateStatusBar('保存错误');
                    });
                }

                function downloadJSONFile(data, filename) {
                    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
                    const url = URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = filename;
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                }
                
                function showModManagement() {
                    document.getElementById('welcomeSection').style.display = 'none';
                    document.getElementById('modManagementSection').style.display = 'flex';
                    document.getElementById('statsDisplay').style.display = 'flex';
                }
                
                function showWelcome() {
                    document.getElementById('welcomeSection').style.display = 'flex';
                    document.getElementById('modManagementSection').style.display = 'none';
                    document.getElementById('statsDisplay').style.display = 'none';
                }
                
                function updateStats(stats) {
                    document.getElementById('statTotalMods').textContent = stats.total_mods;
                    document.getElementById('statEnabledMods').textContent = stats.enabled_mods;
                    document.getElementById('statDisabledMods').textContent = stats.disabled_mods;
                    document.getElementById('statUnsavedChanges').textContent = stats.has_unsaved_changes ? '是' : '否';
                    
                    // 根据是否有未保存更改改变颜色
                    const unsavedElement = document.getElementById('statUnsavedChanges');
                    unsavedElement.style.color = stats.has_unsaved_changes ? '#e74c3c' : '#2c3e50';
                }
                
                function renderModList() {
                    const modList = document.getElementById('modList');
                    
                    if (currentMods.length === 0) {
                        modList.innerHTML = `
                            <div class="empty-state">
                                <div class="empty-state-icon">📁</div>
                                <p>没有模组数据</p>
                            </div>
                        `;
                        return;
                    }
                    
                    let html = '';
                    currentMods.forEach((mod, index) => {
                        const enabledClass = mod.enabled ? 'enabled' : 'disabled';
                        const webUrl = mod.web_url ? `<a href="${mod.web_url}" target="_blank" class="mod-url">查看</a>` : '-';
                        
                        html += `
                            <div class="mod-item ${enabledClass}" data-mod-key="${mod.key}">
                                <input type="checkbox" class="mod-checkbox" ${mod.enabled ? 'checked' : ''} 
                                       onchange="toggleMod('${mod.key}', this.checked)">
                                <div>
                                    <div class="mod-name">${mod.friendly_name}</div>
                                    <div class="mod-id">${mod.key}</div>
                                </div>
                                <div class="mod-priority">#${mod.priority}</div>
                                <div class="mod-type">${mod.mod_type}</div>
                                <div class="mod-url">${webUrl}</div>
                            </div>
                        `;
                    });
                    
                    modList.innerHTML = html;
                }
                
                function toggleMod(modKey, enabled) {
                    pywebview.api.handle_mod_toggle(modKey, enabled).then(response => {
                        if (response.success) {
                            // 更新本地数据
                            const mod = currentMods.find(m => m.key === modKey);
                            if (mod) {
                                mod.enabled = enabled;
                            }
                            updateStats(response.stats);
                            renderModList(); // 重新渲染以更新样式
                        } else {
                            showStatus(response.message, 'error');
                        }
                    }).catch(error => {
                        showStatus('切换模组状态时发生错误: ' + error, 'error');
                    });
                }
                
                function reorderMods() {
                    showStatus('重新排序功能开发中...', 'info');
                }
                
                // 初始化
                document.addEventListener('DOMContentLoaded', function() {
                    console.log('模组管理器界面已加载');
                    updateStatusBar('就绪');
                    setupDragAndDrop();
                    setupContextMenu();
                    
                    // 尝试自动加载测试文件
                    setTimeout(() => {
                        loadTestFiles();
                    }, 500);
                });

                function loadTestFiles() {
                    // 尝试从后端获取测试文件内容
                    pywebview.api.get_test_files().then(response => {
                        if (response.success && response.has_test_files) {
                            showStatus('检测到测试文件，正在自动加载...', 'info');
                            
                            // 使用测试文件数据
                            currentModActiveData = response.mod_active_data;
                            currentPriorityData = response.priority_data;
                            currentModActiveFileName = 'test_mod_active.json';
                            currentPriorityFileName = 'test_priority.json';
                            
                            document.getElementById('modActiveFileInfo').textContent = currentModActiveFileName;
                            document.getElementById('priorityFileInfo').textContent = currentPriorityFileName;
                            
                            // 自动加载
                            setTimeout(() => {
                                loadModFiles();
                            }, 1000);
                        }
                    }).catch(error => {
                        console.log('未找到测试文件或加载失败:', error);
                    });
                }
                
                // 拖拽排序功能
                function setupDragAndDrop() {
                    const modList = document.getElementById('modList');
                    if (!modList) return;
                    
                    modList.addEventListener('mousedown', handleMouseDown);
                    document.addEventListener('mousemove', handleMouseMove);
                    document.addEventListener('mouseup', handleMouseUp);
                }
                
                function handleMouseDown(e) {
                    // 检查是否在模组项上点击
                    const modItem = e.target.closest('.mod-item');
                    if (!modItem) {
                        // 在空白区域开始框选
                        if (e.button === 0) { // 左键
                            startMultiSelect(e);
                        }
                        return;
                    }
                    
                    const modKey = modItem.getAttribute('data-mod-key');
                    
                    // Ctrl+点击多选
                    if (e.ctrlKey) {
                        e.preventDefault();
                        toggleModSelection(modKey);
                        return;
                    }
                    
                    // Shift+点击连续选择
                    if (e.shiftKey) {
                        e.preventDefault();
                        selectModRange(modKey);
                        return;
                    }
                    
                    // 普通点击：清除选择并选择当前项
                    if (!selectedMods.has(modKey)) {
                        clearSelection();
                        selectMod(modKey);
                    }
                    
                    // 开始拖拽
                    startDrag(e, modItem);
                }
                
                function startMultiSelect(e) {
                    isMultiSelecting = true;
                    dragStartX = e.clientX;
                    dragStartY = e.clientY;
                    
                    // 创建选择矩形
                    selectionRectangle = document.createElement('div');
                    selectionRectangle.className = 'selection-rectangle';
                    selectionRectangle.style.left = dragStartX + 'px';
                    selectionRectangle.style.top = dragStartY + 'px';
                    document.body.appendChild(selectionRectangle);
                    
                    // 清除当前选择
                    clearSelection();
                }
                
                function handleMouseMove(e) {
                    if (isMultiSelecting) {
                        updateSelectionRectangle(e);
                        updateMultiSelection();
                    } else if (isDragging) {
                        updateDragPosition(e);
                    }
                }
                
                function handleMouseUp(e) {
                    if (isMultiSelecting) {
                        endMultiSelect();
                    } else if (isDragging) {
                        endDrag(e);
                    }
                }
                
                function updateSelectionRectangle(e) {
                    if (!selectionRectangle) return;
                    
                    const currentX = e.clientX;
                    const currentY = e.clientY;
                    
                    const left = Math.min(dragStartX, currentX);
                    const top = Math.min(dragStartY, currentY);
                    const width = Math.abs(currentX - dragStartX);
                    const height = Math.abs(currentY - dragStartY);
                    
                    selectionRectangle.style.left = left + 'px';
                    selectionRectangle.style.top = top + 'px';
                    selectionRectangle.style.width = width + 'px';
                    selectionRectangle.style.height = height + 'px';
                }
                
                function updateMultiSelection() {
                    if (!selectionRectangle) return;
                    
                    const rect = selectionRectangle.getBoundingClientRect();
                    const modItems = document.querySelectorAll('.mod-item');
                    
                    modItems.forEach(item => {
                        const itemRect = item.getBoundingClientRect();
                        const modKey = item.getAttribute('data-mod-key');
                        
                        // 检查模组项是否与选择矩形相交
                        if (rectsIntersect(rect, itemRect)) {
                            selectMod(modKey);
                        }
                    });
                }
                
                function rectsIntersect(rect1, rect2) {
                    return !(rect1.right < rect2.left || 
                            rect1.left > rect2.right || 
                            rect1.bottom < rect2.top || 
                            rect1.top > rect2.bottom);
                }
                
                function endMultiSelect() {
                    isMultiSelecting = false;
                    if (selectionRectangle) {
                        selectionRectangle.remove();
                        selectionRectangle = null;
                    }
                    updateMultiSelectToolbar();
                }
                
                function startDrag(e, modItem) {
                    isDragging = true;
                    modItem.classList.add('dragging');
                    
                    // 设置拖拽图像
                    e.dataTransfer?.setData('text/plain', '');
                    e.dataTransfer.effectAllowed = 'move';
                }
                
                function updateDragPosition(e) {
                    // 更新拖拽视觉反馈
                    const modItems = document.querySelectorAll('.mod-item');
                    const draggingItem = document.querySelector('.mod-item.dragging');
                    
                    if (!draggingItem) return;
                    
                    modItems.forEach(item => {
                        if (item !== draggingItem) {
                            const rect = item.getBoundingClientRect();
                            if (e.clientY < rect.bottom && e.clientY > rect.top) {
                                item.classList.add('drag-over');
                            } else {
                                item.classList.remove('drag-over');
                            }
                        }
                    });
                }
                
                function endDrag(e) {
                    isDragging = false;
                    
                    const draggingItem = document.querySelector('.mod-item.dragging');
                    if (!draggingItem) return;
                    
                    draggingItem.classList.remove('dragging');
                    
                    // 找到放置目标
                    const dragOverItems = document.querySelectorAll('.mod-item.drag-over');
                    if (dragOverItems.length > 0) {
                        const targetItem = dragOverItems[0];
                        const draggedModKey = draggingItem.getAttribute('data-mod-key');
                        const targetModKey = targetItem.getAttribute('data-mod-key');
                        
                        // 重新排序
                        reorderMods(draggedModKey, targetModKey);
                    }
                    
                    // 清除拖拽状态
                    document.querySelectorAll('.mod-item').forEach(item => {
                        item.classList.remove('drag-over');
                    });
                }
                
                // 选择管理功能
                function selectMod(modKey) {
                    selectedMods.add(modKey);
                    const modItem = document.querySelector(`[data-mod-key="${modKey}"]`);
                    if (modItem) {
                        modItem.classList.add('selected');
                    }
                }
                
                function toggleModSelection(modKey) {
                    if (selectedMods.has(modKey)) {
                        selectedMods.delete(modKey);
                        const modItem = document.querySelector(`[data-mod-key="${modKey}"]`);
                        if (modItem) {
                            modItem.classList.remove('selected');
                        }
                    } else {
                        selectMod(modKey);
                    }
                    updateMultiSelectToolbar();
                }
                
                function selectModRange(targetModKey) {
                    if (selectedMods.size === 0) {
                        selectMod(targetModKey);
                        return;
                    }
                    
                    const modKeys = currentMods.map(mod => mod.key);
                    const selectedArray = Array.from(selectedMods);
                    const lastSelected = selectedArray[selectedArray.length - 1];
                    const startIndex = modKeys.indexOf(lastSelected);
                    const endIndex = modKeys.indexOf(targetModKey);
                    
                    if (startIndex === -1 || endIndex === -1) return;
                    
                    const start = Math.min(startIndex, endIndex);
                    const end = Math.max(startIndex, endIndex);
                    
                    for (let i = start; i <= end; i++) {
                        selectMod(modKeys[i]);
                    }
                    updateMultiSelectToolbar();
                }
                
                function clearSelection() {
                    selectedMods.clear();
                    document.querySelectorAll('.mod-item').forEach(item => {
                        item.classList.remove('selected');
                    });
                    updateMultiSelectToolbar();
                }
                
                function updateMultiSelectToolbar() {
                    const toolbar = document.getElementById('multiSelectToolbar');
                    const countElement = document.getElementById('multiSelectCount');
                    
                    if (selectedMods.size > 0) {
                        toolbar.classList.add('show');
                        countElement.textContent = `已选择 ${selectedMods.size} 个模组`;
                    } else {
                        toolbar.classList.remove('show');
                    }
                }
                
                // 多选操作功能
                function enableSelectedMods() {
                    const modKeys = Array.from(selectedMods);
                    pywebview.api.handle_batch_toggle(modKeys, true).then(response => {
                        if (response.success) {
                            // 更新本地数据
                            modKeys.forEach(modKey => {
                                const mod = currentMods.find(m => m.key === modKey);
                                if (mod) mod.enabled = true;
                            });
                            updateStats(response.stats);
                            renderModList();
                            showStatus(response.message, 'success');
                        } else {
                            showStatus(response.message, 'error');
                        }
                    });
                }
                
                function disableSelectedMods() {
                    const modKeys = Array.from(selectedMods);
                    pywebview.api.handle_batch_toggle(modKeys, false).then(response => {
                        if (response.success) {
                            // 更新本地数据
                            modKeys.forEach(modKey => {
                                const mod = currentMods.find(m => m.key === modKey);
                                if (mod) mod.enabled = false;
                            });
                            updateStats(response.stats);
                            renderModList();
                            showStatus(response.message, 'success');
                        } else {
                            showStatus(response.message, 'error');
                        }
                    });
                }
                
                function moveSelectedToTop() {
                    const modKeys = Array.from(selectedMods);
                    pywebview.api.handle_move_to_top(modKeys).then(response => {
                        if (response.success) {
                            // 更新本地数据
                            const selectedModsList = currentMods.filter(mod => modKeys.includes(mod.key));
                            const otherMods = currentMods.filter(mod => !modKeys.includes(mod.key));
                            currentMods = selectedModsList.concat(otherMods);
                            
                            // 更新优先级
                            currentMods.forEach((mod, index) => {
                                mod.priority = index;
                            });
                            
                            updateStats(response.stats);
                            renderModList();
                            clearSelection();
                            showStatus(response.message, 'success');
                        } else {
                            showStatus(response.message, 'error');
                        }
                    });
                }
                
                function moveSelectedToBottom() {
                    const modKeys = Array.from(selectedMods);
                    pywebview.api.handle_move_to_bottom(modKeys).then(response => {
                        if (response.success) {
                            // 更新本地数据
                            const selectedModsList = currentMods.filter(mod => modKeys.includes(mod.key));
                            const otherMods = currentMods.filter(mod => !modKeys.includes(mod.key));
                            currentMods = otherMods.concat(selectedModsList);
                            
                            // 更新优先级
                            currentMods.forEach((mod, index) => {
                                mod.priority = index;
                            });
                            
                            updateStats(response.stats);
                            renderModList();
                            clearSelection();
                            showStatus(response.message, 'success');
                        } else {
                            showStatus(response.message, 'error');
                        }
                    });
                }
                
                // 修改renderModList函数以支持拖拽
                function renderModList() {
                    const modList = document.getElementById('modList');
                    
                    if (currentMods.length === 0) {
                        modList.innerHTML = `
                            <div class="empty-state">
                                <div class="empty-state-icon">📁</div>
                                <p>没有模组数据</p>
                            </div>
                        `;
                        return;
                    }
                    
                    let html = '';
                    currentMods.forEach((mod, index) => {
                        const enabledClass = mod.enabled ? 'enabled' : 'disabled';
                        const selectedClass = selectedMods.has(mod.key) ? 'selected' : '';
                        const webUrl = mod.web_url ? `<a href="${mod.web_url}" target="_blank" class="mod-url">查看</a>` : '-';
                        
                        html += `
                            <div class="mod-item ${enabledClass} ${selectedClass}" data-mod-key="${mod.key}">
                                <div class="drag-handle">☰</div>
                                <input type="checkbox" class="mod-checkbox" ${mod.enabled ? 'checked' : ''} 
                                    onchange="toggleMod('${mod.key}', this.checked)">
                                <div>
                                    <div class="mod-name">${mod.friendly_name}</div>
                                    <div class="mod-id">${mod.key}</div>
                                </div>
                                <div class="mod-priority">#${mod.priority}</div>
                                <div class="mod-type">${mod.mod_type}</div>
                                <div class="mod-url">${webUrl}</div>
                            </div>
                        `;
                    });
                    
                    modList.innerHTML = html;
                    
                    // 重新设置拖拽事件
                    setTimeout(setupDragAndDrop, 0);
                }
                
                // 修改初始化函数
                document.addEventListener('DOMContentLoaded', function() {
                    console.log('模组管理器界面已加载');
                    updateStatusBar('就绪');
                    setupDragAndDrop();
                    
                    // 测试文件自动加载...
                });

                let contextMenuTarget = null;

                // 右键菜单功能
                function setupContextMenu() {
                    document.addEventListener('contextmenu', handleContextMenu);
                    document.addEventListener('click', hideContextMenu);
                }

                function handleContextMenu(e) {
                    const modItem = e.target.closest('.mod-item');
                    if (modItem) {
                        e.preventDefault();
                        contextMenuTarget = modItem.getAttribute('data-mod-key');
                        
                        // 如果右键的模组不在选择中，清除选择并选择它
                        if (!selectedMods.has(contextMenuTarget)) {
                            clearSelection();
                            selectMod(contextMenuTarget);
                        }
                        
                        showContextMenu(e.clientX, e.clientY);
                    } else {
                        hideContextMenu();
                    }
                }

                function showContextMenu(x, y) {
                    const contextMenu = document.getElementById('contextMenu');
                    contextMenu.style.display = 'block';
                    
                    // 确保菜单位置在可视区域内
                    const rect = contextMenu.getBoundingClientRect();
                    const viewportWidth = window.innerWidth;
                    const viewportHeight = window.innerHeight;
                    
                    let adjustedX = x;
                    let adjustedY = y;
                    
                    if (x + rect.width > viewportWidth) {
                        adjustedX = viewportWidth - rect.width - 10;
                    }
                    
                    if (y + rect.height > viewportHeight) {
                        adjustedY = viewportHeight - rect.height - 10;
                    }
                    
                    contextMenu.style.left = adjustedX + 'px';
                    contextMenu.style.top = adjustedY + 'px';
                }

                function hideContextMenu() {
                    const contextMenu = document.getElementById('contextMenu');
                    contextMenu.style.display = 'none';
                    contextMenuTarget = null;
                }

                function contextMenuEnable() {
                    enableSelectedMods();
                    hideContextMenu();
                }

                function contextMenuDisable() {
                    disableSelectedMods();
                    hideContextMenu();
                }

                function contextMenuMoveToTop() {
                    moveSelectedToTop();
                    hideContextMenu();
                }

                function contextMenuMoveToBottom() {
                    moveSelectedToBottom();
                    hideContextMenu();
                }

                // 在初始化时设置右键菜单
                document.addEventListener('DOMContentLoaded', function() {
                    // ... 其他初始化代码
                    setupContextMenu();
                });

                // 添加快捷键支持
                function setupKeyboardShortcuts() {
                    document.addEventListener('keydown', function(e) {
                        // Ctrl+S 保存
                        if (e.ctrlKey && e.key === 's') {
                            e.preventDefault();
                            if (!document.getElementById('saveBtn').disabled) {
                                saveModFiles();
                            }
                        }
                        
                        // Ctrl+O 打开文件
                        if (e.ctrlKey && e.key === 'o') {
                            e.preventDefault();
                            document.getElementById('modActiveFile').click();
                        }
                        
                        // Ctrl+A 全选（仅在模组列表可见时）
                        if (e.ctrlKey && e.key === 'a' && document.getElementById('modManagementSection').style.display !== 'none') {
                            e.preventDefault();
                            selectAllMods();
                        }
                        
                        // Escape 清除选择
                        if (e.key === 'Escape') {
                            clearSelection();
                        }
                    });
                }

                function selectAllMods() {
                    clearSelection();
                    currentMods.forEach(mod => {
                        selectMod(mod.key);
                    });
                    updateMultiSelectToolbar();
                }

                // 更新初始化函数
                document.addEventListener('DOMContentLoaded', function() {
                    console.log('模组管理器界面已加载');
                    updateStatusBar('就绪');
                    setupDragAndDrop();
                    setupContextMenu();
                    setupKeyboardShortcuts();
                    
                    // 尝试自动加载测试文件
                    setTimeout(() => {
                        loadTestFiles();
                    }, 500);
                });
            </script>
        </body>
        </html>
        """
        return html