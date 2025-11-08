from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #ffffff;")

        layout = QVBoxLayout(self)
        title = QLabel("▶ 首页")
        title.setFont(QFont("Microsoft YaHei", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #333; padding: 20px;")
        layout.addWidget(title)


class SettingsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #f8f9fa;")

        layout = QVBoxLayout(self)
        title = QLabel("▶ 设置")
        title.setFont(QFont("Microsoft YaHei", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #333; padding: 20px;")
        layout.addWidget(title)


class AboutPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #e9ecef;")

        layout = QVBoxLayout(self)
        title = QLabel("▶ 关于")
        title.setFont(QFont("Microsoft YaHei", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #333; padding: 20px;")
        layout.addWidget(title)


class DebugPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #dee2e6;")

        layout = QVBoxLayout(self)

        # 标题
        title = QLabel("▶ 调试页面")
        title.setFont(QFont("Microsoft YaHei", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #333; padding: 16px 20px;")
        layout.addWidget(title)

        # 第一行：按钮一 + 文本框一
        row1 = QHBoxLayout()
        btn1 = QPushButton("运行函数一")
        btn1.setFixedHeight(36)
        self.output1 = QTextEdit()
        self.output1.setReadOnly(True)
        self.output1.setPlaceholderText("函数一输出将显示在此处...")
        self.output1.setFixedHeight(80)
        row1.addWidget(btn1)
        row1.addWidget(self.output1)
        layout.addLayout(row1)

        # 第二行：按钮二 + 文本框二
        row2 = QHBoxLayout()
        btn2 = QPushButton("运行函数二")
        btn2.setFixedHeight(36)
        self.output2 = QTextEdit()
        self.output2.setReadOnly(True)
        self.output2.setPlaceholderText("函数二输出将显示在此处...")
        self.output2.setFixedHeight(80)
        row2.addWidget(btn2)
        row2.addWidget(self.output2)
        layout.addLayout(row2)

        # 第三行：按钮三 + 文本框三
        row3 = QHBoxLayout()
        btn3 = QPushButton("运行函数三")
        btn3.setFixedHeight(36)
        self.output3 = QTextEdit()
        self.output3.setReadOnly(True)
        self.output3.setPlaceholderText("函数三输出将显示在此处...")
        self.output3.setFixedHeight(80)
        row3.addWidget(btn3)
        row3.addWidget(self.output3)
        layout.addLayout(row3)

        # 第四行：按钮四 + 文本框四
        row4 = QHBoxLayout()
        btn4 = QPushButton("运行函数四")
        btn4.setFixedHeight(36)
        self.output4 = QTextEdit()
        self.output4.setReadOnly(True)
        self.output4.setPlaceholderText("函数四输出将显示在此处...")
        self.output4.setFixedHeight(80)
        row4.addWidget(btn4)
        row4.addWidget(self.output4)
        layout.addLayout(row4)

        # 第五行：按钮五 + 文本框五
        row5 = QHBoxLayout()
        btn5 = QPushButton("运行函数五")
        btn5.setFixedHeight(36)
        self.output5 = QTextEdit()
        self.output5.setReadOnly(True)
        self.output5.setPlaceholderText("函数五输出将显示在此处...")
        self.output5.setFixedHeight(80)
        row5.addWidget(btn5)
        row5.addWidget(self.output5)
        layout.addLayout(row5)

        # 信号连接
        btn1.clicked.connect(self.on_btn1_clicked)
        btn2.clicked.connect(self.on_btn2_clicked)
        btn3.clicked.connect(self.on_btn3_clicked)
        btn4.clicked.connect(self.on_btn4_clicked)
        btn5.clicked.connect(self.on_btn5_clicked)

    # 示例函数与槽，可替换为实际业务逻辑
    def on_btn1_clicked(self):
        try:
            result = self.debug_func_one()
        except Exception as e:
            result = f"执行函数一发生错误：{e}"
        self.output1.setPlainText(str(result))

    def on_btn2_clicked(self):
        try:
            result = self.debug_func_two()
        except Exception as e:
            result = f"执行函数二发生错误：{e}"
        self.output2.setPlainText(str(result))

    def on_btn3_clicked(self):
        try:
            result = self.debug_func_three()
        except Exception as e:
            result = f"执行函数三发生错误：{e}"
        self.output3.setPlainText(str(result))

    def on_btn4_clicked(self):
        try:
            result = self.debug_func_four()
        except Exception as e:
            result = f"执行函数四发生错误：{e}"
        self.output4.setPlainText(str(result))

    def on_btn5_clicked(self):
        try:
            result = self.debug_func_five()
        except Exception as e:
            result = f"执行函数五发生错误：{e}"
        self.output5.setPlainText(str(result))

    def debug_func_one(self):
        return "函数一已执行：这是示例输出。"

    def debug_func_two(self):
        return "函数二已执行：这是另一个示例输出。"

    def debug_func_three(self):
        return "函数三已执行：占位示例输出。"

    def debug_func_four(self):
        return "函数四已执行：占位示例输出。"

    def debug_func_five(self):
        return "函数五已执行：占位示例输出。"