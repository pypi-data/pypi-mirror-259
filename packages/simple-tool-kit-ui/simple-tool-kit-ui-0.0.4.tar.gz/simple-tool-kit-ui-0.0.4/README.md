# 工具配置流程

制作中...

## 上传package

使用cd 进入pyproject.toml所在文件夹内

依次执行一下几个命令

```commandline
python -m build

twine check dist/*

twine upload dist/*
```