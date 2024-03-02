from setuptools import setup, find_packages

setup(
    name='aliyun_logger',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'aliyun-log-python-sdk',
        'enum34'
    ],
    author='Yuxiang Zhang',
    author_email='zhangyuxiang@53zaixian.com',
    description='Python package for 53 Aliyun Logger',
    url='https://github.com/your_username/aliyun-logger',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
