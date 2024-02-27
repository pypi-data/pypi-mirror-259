import sys
from enum import Enum

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from tool_kit.category_detail_widget import CategoryDetailWidget
from tool_kit.category_list_widget import CategoryListWidget
from tool_kit.register import find_tools_by_package_name, get_main_module_name, get_doc_dir

global_window = None


class MainUI(QMainWindow):
    def __init__(self, category: Enum = None):
        super().__init__()
        package_name = get_main_module_name()
        doc_dir = get_doc_dir()  # 存放工作流程的帮助文档的dir路径
        tools = find_tools_by_package_name(package_name)  # 被管理的工具的子类列表

        self.main_layout = QHBoxLayout()



        self.category_detail_widget = CategoryDetailWidget(
            title='Category Detail',
        )

        self.category_list_widget = CategoryListWidget(
            title='Category List',
            category=category,
            category_detail_widget=self.category_detail_widget,
            tool_list=tools,
            doc_dir=doc_dir,
        )

        self.main_layout.addWidget(self.category_list_widget)
        self.main_layout.addWidget(self.category_detail_widget)
        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)

        self.setCentralWidget(central_widget)


def main_dev():
    '''
    非UI测试
    '''
    app = QApplication([])
    main_ui = MainUI()
    main_ui.show()
    app.exec()


def main():
    global global_window
    app = QApplication.instance() or QApplication(sys.argv)
    if global_window:
        global_window.show()
    else:
        global_window = MainUI()
        global_window.show()
    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)


if __name__ == '__main__':
    main_dev()
