import importlib
import os
import pkgutil
import sys
from tool_kit.tool_config import ToolConfigBase


def find_modules_by_package_name(package_name: str) -> list[str]:
    # 配置package名称
    package_name = package_name.lower()
    # 动态导入嵌套包
    nested_package = __import__(package_name, fromlist=[''])

    # 获取嵌套包的文件路径
    nested_package_path = nested_package.__path__

    # 遍历嵌套包中的所有模块
    modules = [name for _, name, _ in pkgutil.iter_modules(nested_package_path)]

    return modules


def find_tools_by_package_name(package_name: str) -> list[ToolConfigBase]:
    '''
    返回工具的子类的列表
    :param package_name:
    :return:
    '''
    result = []
    for module_name in find_modules_by_package_name(package_name=package_name):
        class_name = ToolConfigBase.__subclass_name__()
        package_module_path = f'{package_name}.{module_name}'
        module = importlib.import_module(package_module_path)
        if hasattr(module, class_name):
            print("~" * 30)
            print(module, class_name)
            cls = getattr(module, class_name)()
            result.append(cls)
    return result


def get_main_module_name() -> str:
    base_name, _ = os.path.splitext(os.path.basename(sys.argv[0]))
    return base_name


def get_main_module_path() -> str:
    """
    获取主程序的path
    :return:
    """
    return sys.argv[0]


def get_doc_dir() -> str:
    """
    获取doc的路径
    :return:
    """
    main_module_path = get_main_module_path()

    dir_path = os.path.join(os.path.dirname(main_module_path), ToolConfigBase.__tool_doc_dir_name__())
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path
