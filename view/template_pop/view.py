# -*- coding: utf-8 -*-
import os,sys
_top = sys.modules['__main__']
import ollama
from view.template_pop._view import Ui_Form
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread,Signal,QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QWidget, QDialog)
import requests

remote_host = _top.config['ai']['host']  # Replace with your actual remote server URL
client = ollama.Client(host=remote_host)

def parse_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.replace('\n\n', '')
        return text
    
raw_context = parse_text(_top.config['ai']['doc'])
# print(context)

class LLM(QThread):
    result_signal = Signal(str)
    def __init__(self, context, question):
        super(LLM, self).__init__()
        self.context = context
        self.question=question

    def run(self):
        print(self.context)
        print(self.question)
        try:
            stream = client.chat(
            model="deepseek-r1:7b",  # Replace with the model available on the remote server
            messages = [
                {"role": "system", "content": "你是一个助手,请检索上下文内容, 回答用户提的问题. 回答尽量准确简短, 不要输出<think>内容, 如果没查到就输出\"在上下文未找到答案\", 不要过度联想."},
                {"role": "user", "content": f"上下文: {self.context}\n\n 问题:{self.question}"}
            ],
            stream=True
            )
            for chunk in stream:
                answer=chunk["message"]["content"]
                # print(answer)
                self.result_signal.emit(answer)  # 发送请求结果的信号
        except requests.RequestException as e:
            self.result_signal.emit('Error: ' + str(e))  # 发送请求错误的信号

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.llm = LLM("context","hello")
        self.llm.result_signal.connect(self.on_result)
        self.ui.btn_ask.clicked.connect(self.on_click)
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    color: #333;
                }
                h1 {
                    color: #ff5733;
                }
                p {
                    font-size: 16px;
                    line-height: 1.5;
                }
                .highlight {
                    background-color: yellow;
                }
            </style>
        </head>
        <body>
            <h1>标题</h1>
            <p>这是一个段落，<span class="highlight">部分文字高亮显示</span>。</p>
        </body>
        </html>
        """
        self.ui.tb_answer.setHtml(html_content)

    def on_result(self, result):
        # self.ui.tb_answer.appendHtml(result)
        self.ui.tb_answer.insertPlainText(result)  # 使用 insertPlainText 逐字插入
        # self.ui.tb_answer.moveCursor(self.ui.tb_answer.textCursor().End) 

    def on_click(self):
        self.ui.tb_answer.clear()
        context = raw_context if self.ui.ck_manual.isChecked() else ""
        question = self.ui.tb_quest.text()
        self.ui.tb_answer.insertPlainText(f"正在思考您得问题:{question}...") 
        self.llm = LLM(context=context, question=question)
        self.llm.result_signal.connect(self.on_result)
        self.llm.start()

