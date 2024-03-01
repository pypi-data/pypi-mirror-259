from setuptools import setup, find_packages  

setup(  
    name='jinjinUtils',  
    version='0.1',  
    packages=find_packages(),  
    url='https://gitee.com/wang_chaojin/jinjinutils.git',  
    license='MIT',  
    author='jinjin',  
    author_email='745381270@qq.com',  
    description='处理问题的一些小工具',  
    install_requires=[  
        "pymysql"
    ],  
)