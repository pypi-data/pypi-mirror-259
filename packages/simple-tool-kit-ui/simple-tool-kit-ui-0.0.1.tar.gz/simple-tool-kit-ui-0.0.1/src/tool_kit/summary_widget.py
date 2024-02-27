from PySide6.QtWidgets import QVBoxLayout, QPushButton

from pyproj.src.tool_kit.base_widgets import CustomGrouBox


class SummaryWidget(CustomGrouBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        help_page_bt = QPushButton('Help Page')
        layout.addWidget(help_page_bt)
