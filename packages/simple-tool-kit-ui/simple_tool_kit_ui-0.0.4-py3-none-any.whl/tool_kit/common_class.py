from enum import Enum

from PySide6.QtGui import QStandardItem, QFont
from PySide6.QtWidgets import QWidget, QMessageBox

from tool_kit.tool_config import ToolConfigBase


class CustomToolStandardItem(QStandardItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.tool_item: ToolConfigBase = None


class CustomToolCategoryItem(QStandardItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        为列表布局制作的自定义item。用于储存自定义数据
        """
        self.category: Enum = None

        self.setEditable(False)
        self.setFont(QFont("Arial"))


def show_confirm_dialog(parent: QWidget, msg: str = "Confirm messages", title="Confirm Window") -> bool:
    message_box = QMessageBox(parent)

    message_box.setText(msg)
    message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    message_box.setDefaultButton(QMessageBox.Yes)
    message_box.setWindowTitle(title)
    result = message_box.exec()
    if result == QMessageBox.Yes:
        return True
    else:
        return False
