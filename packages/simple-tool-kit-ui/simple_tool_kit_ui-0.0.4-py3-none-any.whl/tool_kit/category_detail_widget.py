import os.path

from PySide6.QtCore import QModelIndex, Qt, QPoint
from PySide6.QtGui import QStandardItemModel, QAction
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QListView, QTextBrowser, QMenu

from tool_kit.base_widgets import CustomGrouBox
from tool_kit.common_class import CustomToolStandardItem, CustomToolCategoryItem, show_confirm_dialog
from tool_kit.register import get_doc_dir
from tool_kit.tool_config import ToolConfigBase, CustomAction


class CategoryDetailWidget(CustomGrouBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        QHBoxLayout(self)
        # 设置工具区域
        tool_layout = QVBoxLayout()


        self.tool_list_widget = ToolListWidget(title='Tool List')
        tool_layout.addWidget(self.tool_list_widget)

        self.layout().addLayout(tool_layout)


class ToolListWidget(CustomGrouBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)
        self.tool_detail_widget = ToolDescriptionWidget(title='Tool Description')

        self.list_view = QListView()
        self.list_model = QStandardItemModel(self.list_view)

        self.list_view.clicked.connect(self.on_tool_selected)

        self.list_view.setModel(self.list_model)
        self.layout().addWidget(self.list_view)
        self.layout().addWidget(self.tool_detail_widget)

    def update_tool_list(self, tool_list: list[ToolConfigBase], current_selected_category_item: CustomToolCategoryItem):
        self.list_model.clear()
        print("list_model")

        for tool in tool_list:
            for j in tool.get_category():
                if current_selected_category_item.category.value == j.value:
                    item = CustomToolStandardItem(tool.get_tool_name())
                    item.tool_item = tool
                    self.list_model.appendRow(item)

        self.list_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list_view.customContextMenuRequested.connect(self.open_menu)

    def open_menu(self, position: QPoint):
        print("open_menu")

        menu = QMenu(self)

        item: QModelIndex = self.list_view.indexAt(position)
        tool: CustomToolStandardItem = self.list_model.item(item.row())
        for i in tool.tool_item.actions:
            action = QAction(f"{i.action_name}", self)
            action.triggered.connect(
                lambda checked=False, custom_action=i: self.action_triggered(custom_action))
            menu.addAction(action)

        menu.exec_(self.list_view.viewport().mapToGlobal(position))

    def action_triggered(self, custom_action: CustomAction):
        print(custom_action.action_name)
        if not custom_action.start_confirm:
            custom_action.method()
        else:
            if show_confirm_dialog(None):
                custom_action.method()

    def on_tool_selected(self, model_index: QModelIndex):
        """
        选择工具后所触发的动作
        :param model_index:
        :return:
        """
        item: CustomToolStandardItem = self.list_model.item(model_index.row())
        self.tool_detail_widget.update_tool_description(item)


class ToolDescriptionWidget(CustomGrouBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)

        self.description_widget = QTextBrowser()
        self.description_widget.setReadOnly(True)
        self.description_widget.setOpenExternalLinks(True)
        self.layout().addWidget(self.description_widget)

    def update_tool_description(self, current_selected_tool: CustomToolStandardItem):
        # 尝试获取md文档的路径
        md_name = current_selected_tool.tool_item.get_tool_information().tool_description_md_name
        doc_dir = get_doc_dir()
        try:
            md_filepath = os.path.join(doc_dir, md_name)
            with open(md_filepath, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()
                # html_content = markdown.markdown(md_content)
            self.description_widget.setMarkdown(md_content)
        except TypeError:
            self.description_widget.setText(current_selected_tool.tool_item.get_tool_information_summary())

        except Exception as e:
            self.description_widget.setText(str(e))

    def clear_description(self):
        self.description_widget.clear()
