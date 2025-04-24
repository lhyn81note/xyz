import sys
import json
from threading import Thread
from time import sleep
from PySide6.QtCore import Qt, QUrl, QObject, Signal, Slot
from PySide6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebChannel import QWebChannel

# 通信桥梁类
class WebBridge(QObject):
    updateContent = Signal(str)  # 定义更新信号

    def __init__(self):
        super().__init__()
        self._content = ""

    @Slot(str)
    def append_content(self, text):
        """供JavaScript调用的方法"""
        self._content += text
        self.updateContent.emit(self._content)

class BrowserWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # 初始化界面
        self.setup_ui()
        self.setup_web_channel()
        
        # 模拟流式数据生成线程
        self.start_stream_simulation()

    def setup_ui(self):
        """初始化界面布局"""
        self.setWindowTitle("Streaming LLM Response")
        self.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)
        
        self.browser = QWebEngineView()
        self.browser.setHtml(self.get_base_html())  # 加载基础HTML结构
        layout.addWidget(self.browser)

    def setup_web_channel(self):
        """配置Web通信通道"""
        self.web_bridge = WebBridge()
        self.channel = QWebChannel()
        self.channel.registerObject("webBridge", self.web_bridge)
        
        page = self.browser.page()
        page.setWebChannel(self.channel)
        page.loadFinished.connect(self.inject_web_channel)

    def inject_web_channel(self):
        """注入WebChannel初始化脚本"""
        self.browser.page().runJavaScript("""
            new QWebChannel(qt.webChannelTransport, function(channel) {
                window.webBridge = channel.objects.webBridge;
                
                // 初始化内容容器
                const container = document.getElementById('content');
                
                // 连接内容更新信号
                window.webBridge.updateContent.connect(function(text) {
                    container.innerHTML = text.replace(/\n/g, '<br>');
                    window.scrollTo(0, document.body.scrollHeight);
                });
            });
        """)

    def start_stream_simulation(self):
        """启动模拟流式数据生成（替换为实际LLM调用）"""
        def generate_stream():
            responses = [
                "欢迎使用智能助手！", 
                "\n我正在实时处理您的请求...",
                "\n当前系统时间：", 
                "2024-02-20 14:30:00",
                "\n\n以下是分步分析：\n1. 初始化完成\n2. 数据处理中",
                "\n3. 生成最终结果...\n✅ 任务完成！"
            ]
            for text in responses:
                self.web_bridge.append_content(text)
                sleep(0.5)
                
        Thread(target=generate_stream, daemon=True).start()

    @staticmethod
    def get_base_html():
        """生成基础HTML结构"""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    background-color: #121212;
                    color: #ffffff;
                    font-family: 'Segoe UI', sans-serif;
                    line-height: 1.6;
                    padding: 20px;
                    margin: 0;
                }}
                #content {{
                    max-width: 800px;
                    margin: 0 auto;
                    white-space: pre-wrap;
                }}
                .typing-cursor {{
                    display: inline-block;
                    width: 8px;
                    height: 1em;
                    background: #64B5F6;
                    margin-left: 2px;
                    animation: blink 1s infinite;
                }}
                @keyframes blink {{
                    0% {{ opacity: 1; }}
                    50% {{ opacity: 0; }}
                    100% {{ opacity: 1; }}
                }}
            </style>
        </head>
        <body>
            <div id="content"></div>
            <!-- 自动加载Qt的WebChannel支持 -->
            <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
        </body>
        </html>
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec())