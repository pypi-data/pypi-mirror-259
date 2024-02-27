import dataclasses
from dataclasses import dataclass


class _Settings:
    AUTHOR: str = None
    VERSION: str = None
    DESCRIPTION: str = None
    PROJECT_NAME: str = None
    PORT: int = 3000
    HOME_PAGE_URL: str = f'http://localhost:{PORT}/#/'
    DOCS_DIR = "docs"
    # MEMBERS = []

    # 报告bug的地址.出现在工具的概要部分，此处为url时，用户点击此处将自动跳转到相应页面
    BUG_REPORT_URL: str = None
