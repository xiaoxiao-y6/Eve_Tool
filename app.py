# 内置函数导入
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QStackedWidget, QLabel, QPushButton
)
from PyQt6.QtCore import Qt
import os

# # 自定义函数导入
import sys
from src import screen_information_judgment
sys.path.append(r'src')


# ======================================================================================================================================

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("欢迎来到首页！", alignment=Qt.AlignmentFlag.AlignCenter))
        self.setLayout(layout)

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("这是设置页面。", alignment=Qt.AlignmentFlag.AlignCenter))
        self.setLayout(layout)

class Page3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("关于本应用。", alignment=Qt.AlignmentFlag.AlignCenter))
        self.setLayout(layout)

class DebugPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("这是一个调试页面", alignment=Qt.AlignmentFlag.AlignCenter))
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 - EVE_Tool")
        self.resize(800, 600)

        # 主部件
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # 布局
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # 导航栏（左侧）
        self.nav_list = QListWidget()
        self.nav_list.setFixedWidth(150)
        self.nav_list.addItems(["首页", "设置", "关于"])
        self.nav_list.setCurrentRow(0)

        # 页面容器（右侧）
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(Page1())
        self.stacked_widget.addWidget(Page2())
        self.stacked_widget.addWidget(Page3())

        # 连接导航栏和页面切换
        self.nav_list.currentRowChanged.connect(self.stacked_widget.setCurrentIndex)

        # 添加到主布局
        main_layout.addWidget(self.nav_list)
        main_layout.addWidget(self.stacked_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# ======================================================================================================================================












# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QPushButton,
#     QTextEdit, QVBoxLayout, QHBoxLayout
# )
# from PyQt5.QtCore import Qt
# import os



# #####################################################################################################################################################################

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         # 设置窗口标题和大小
#         self.setWindowTitle("EVE_TOOLS")
#         self.resize(600, 400)

#         # 创建按钮
#         self.run_button = QPushButton("执行角色检测")
#         self.run_button.clicked.connect(self.on_button_click)  # 绑定点击事件

#         # 创建文本框（用于显示结果）
#         self.result_text = QTextEdit()
#         self.result_text.setReadOnly(True)  # 设置为只读
#         self.result_text.setPlaceholderText("检测结果将显示在此处...")

#         # 布局
#         layout = QVBoxLayout()
#         layout.addWidget(self.run_button)
#         layout.addWidget(self.result_text)
#         self.setLayout(layout)

#     def on_button_click(self):
#         # 调用你的函数并获取结果
#         result = screen_information_judgment.is_state_active('assets/screenshot_comparison/leave_station_button.png',threshold=float(os.getenv('is_state_active_threshold')))
#         # 将结果写入文本框
#         self.result_text.setPlainText(str(result))

# #####################################################################################################################################################################

# # 启动应用
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())