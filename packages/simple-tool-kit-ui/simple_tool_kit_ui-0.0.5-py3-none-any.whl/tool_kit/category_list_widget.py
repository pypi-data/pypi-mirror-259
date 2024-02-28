from enum import Enum

from PySide6.QtCore import QModelIndex
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QVBoxLayout, QListView

from tool_kit.base_widgets import CustomGrouBox
from tool_kit.category_detail_widget import CategoryDetailWidget
from tool_kit.common_class import CustomToolCategoryItem
from tool_kit.tool_config import ToolConfigBase


class CategoryListWidget(CustomGrouBox):
    def __init__(self, category: Enum = None, tool_list: list[ToolConfigBase] = [],
                 category_detail_widget: CategoryDetailWidget = None,
                 doc_dir: str = None, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.doc_dir = doc_dir
        self.tool_list = tool_list

        self.category_detail_widget = category_detail_widget
        self.category = category
        layout = QVBoxLayout(self)
        self.setMaximumWidth(200)
        self.list_widget = QListView()
        self.list_model = QStandardItemModel(self.list_widget)
        self.list_widget.clicked.connect(self.update_category)
        for i in category:
            item = CustomToolCategoryItem(i.value)
            item.category = i
            self.list_model.appendRow(item)

        self.list_widget.setModel(self.list_model)

        self.layout().addWidget(self.list_widget)

    def update_category(self, item: QModelIndex):
        current_selected_custom_category: CustomToolCategoryItem = self.list_model.item(item.row())
        self.category_detail_widget.tool_list_widget.update_tool_list(self.tool_list, current_selected_custom_category)
        self.category_detail_widget.tool_list_widget.tool_detail_widget.clear_description()
