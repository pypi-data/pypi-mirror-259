from setuptools import setup, find_packages

setup(
    # 以下为必需参数
    name='minj-mark',  # 模块名
    version='1.0.1',  # 当前版本
    description='为图片增加水印',  # 简短描述
    py_modules=["mark"],  # 单文件模块写法
    # 以下均为可选参数
    url='https://github.com/bilibili-ming/mark',  # 主页链接
    author='minj',
    install_requires=['Pillow>=5.1.0']
)