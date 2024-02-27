from PySide6.QtWidgets import QGroupBox, QVBoxLayout


class CustomGrouBox(QGroupBox):
    def __init__(self, title: str = 'DefaultGroupBox', *args, **kwargs):
        super().__init__(title, *args, **kwargs)
