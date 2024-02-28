from PySide6.QtWidgets import QVBoxLayout, QLabel

from tool_kit.base_widgets import CustomGrouBox
from tool_kit.register import get_settings

SETTINGS = get_settings()


class SummaryWidget(CustomGrouBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        layout = QVBoxLayout(self)

        home_page_label = self.make_can_open_external_links_label(
            label_name='Home Page',
            url=SETTINGS.HOME_PAGE_URL,
            content='Open home page')
        home_page_label.setOpenExternalLinks(True)
        project_name_label = QLabel(SETTINGS.PROJECT_NAME)
        version_label = QLabel(f'version: {SETTINGS.VERSION}')

        layout.addWidget(project_name_label)
        layout.addWidget(version_label)

        if SETTINGS.BUG_REPORT_URL:
            rep = QLabel(f'Report: <a href="{SETTINGS.BUG_REPORT_URL}">Click and Report</a>')
            rep.setOpenExternalLinks(True)
            layout.addWidget(rep)

        layout.addWidget(home_page_label)

    @classmethod
    def make_can_open_external_links_label(cls, label_name: str = 'label', url: str = '', content: str = 'content'):
        return QLabel(f'{label_name}: <a href="{url}">{content}</a>')
