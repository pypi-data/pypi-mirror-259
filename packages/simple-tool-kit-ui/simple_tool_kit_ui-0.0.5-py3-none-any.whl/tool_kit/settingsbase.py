import socket
import subprocess
import platform


def is_port_available_direct(port):
    """直接使用socket检查端口是否空闲."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('0.0.0.0', port))
            s.listen(1)
            return True
        except socket.error:
            return False


def is_port_available_external(port):
    """通过调用外部命令检查端口是否空闲."""
    try:
        if platform.system() == "Windows":
            cmd = f"netstat -an | findstr {port}"
        else:
            # 对于Unix和Linux，lsof和netstat都是可用的，这里使用lsof
            cmd = f"lsof -i :{port} || netstat -an | grep {port}"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout == b''  # 如果没有输出，那么端口空闲
    except Exception as e:
        print(f"Error checking port with external command: {e}")
        return False


def is_port_available(port):
    """综合直接和外部方法检查端口是否空闲."""
    if is_port_available_direct(port):
        return True
    else:
        # 如果直接方法失败，尝试外部命令方法
        return is_port_available_external(port)


class Meta(type):
    PORT: int = None  # 端口是否被设置过

    def __init__(cls, name, bases, attrs):
        if not cls.PORT:
            cls.PORT = cls._get_port(3700)
            cls.HOME_PAGE_URL: str = f'http://localhost:{cls.PORT}/#/'

        super().__init__(name, bases, attrs)

    def _get_port(self, port):
        if is_port_available(port):
            return port
        else:
            while not is_port_available(port):
                port += 1
            return port


class SettingsBase(metaclass=Meta):
    # class Meta:
    AUTHOR: str = None
    VERSION: str = None
    DESCRIPTION: str = None
    PROJECT_NAME: str = None

    DOCS_DIR = "docs"
    WINDOW_TITTLE: str = None

    # 报告bug的地址.出现在工具的概要部分，此处为url时，用户点击此处将自动跳转到相应页面
    BUG_REPORT_URL: str = None
