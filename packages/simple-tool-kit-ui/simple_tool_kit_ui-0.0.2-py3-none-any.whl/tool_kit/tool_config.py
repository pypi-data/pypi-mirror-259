import dataclasses
import webbrowser
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum


@dataclass
class ToolInformation:
    tool_name: str = ""
    tool_version: str = ""
    tool_description: str = ""
    tool_description_md_name: str = ""
    tool_author: str = ""
    help_url: str = ""
    report_url: str = ""


@dataclass
class CustomAction:
    action_name: str = "RunAction"
    method: callable = None
    start_confirm: bool = False


class Utilities:

    @classmethod
    def open_url(cls, url):
        webbrowser.open(url)


class AbsModel(Utilities):

    def __init__(self):
        super().__init__()
        self.actions: list[CustomAction] = []  # 动作列表

    class Meta:
        category_list: list[Enum] = []
        report_url: str = None  # 报告问题url，非必要
        help_url: str = None  # 帮助页面url，非必要
        local_help_path: str = None  # 本地帮助文档地址
        tool_name: str = None  # 工具的名字
        tool_version: str = None  # tool version
        tool_description: str = None
        tool_description_md_name: str = None  # 描述工具说明的MD文件存放地址
        tool_author: str = None
        main_action_name: str = None
        main_action: CustomAction = None

        def __init__(self):
            super().__init__()

    def get_tool_information(self):
        return ToolInformation(
            tool_name=self.Meta.tool_name,
            tool_version=self.Meta.tool_version,
            tool_description_md_name=self.Meta.tool_description_md_name,
            tool_description=self.Meta.tool_description,
            tool_author=self.Meta.tool_author,
            help_url=self.Meta.help_url,
            report_url=self.Meta.report_url,

        )

    def get_tool_information_summary(self) -> str:
        result = ""
        result += "-" * 30 + "\n"
        for k, v in dataclasses.asdict(self.get_tool_information()).items():
            if v:
                result += f"{k}:\n{v}" + "\n"
                result += "-" * 10 + "\n"

        return result

    def get_category(self) -> list[Enum]:
        return self.Meta.category_list

    def get_tool_name(self):
        '''
        重写工具的名字
        :return:
        '''
        return self.Meta.tool_name or "DefaultToolName"

    def get_tool_description(self):
        '''
        重写工具的描述文档
        :return:
        '''
        return self.Meta.tool_description or "No Description"

    def add_actions(self):
        if self.Meta.main_action:
            self.actions.append(self.Meta.main_action)

        # 添加打开汇报Bug动作
        if self.Meta.report_url:
            self.actions.append(
                CustomAction(action_name="ReportBugPage", method=lambda: self.open_url(self.Meta.report_url)))

        # 打开帮助页面动作
        if self.Meta.help_url:
            self.actions.append(
                CustomAction(action_name="HelpPage", method=lambda: self.open_url(self.Meta.help_url))
            )

        # 打开本地帮助页面
        if self.Meta.local_help_path:
            self.actions.append(
                CustomAction(action_name="LocalHelpPage", method=lambda: self.open_url(self.Meta.local_help_path))
            )

        # 当没有任何动作时，添加默认动作
        if len(self.actions) == 0:
            self.actions.append(
                CustomAction(action_name="Please Add a Action", method=lambda: print("No Action Selected")))


class ToolConfigBase(ABC, AbsModel):

    def __init__(self):
        super().__init__()
        # 配置默认动作

        self.add_actions()

    @classmethod
    def __subclass_name__(cls) -> str:
        """
        工具模组中的入口子类名
        :return:
        """
        return "ToolConfig"

    @classmethod
    def __tool_doc_dir_name__(cls) -> str:
        '''
        配置md文档的存放在package下的目录名字
        :return:
        '''
        return "docs"
