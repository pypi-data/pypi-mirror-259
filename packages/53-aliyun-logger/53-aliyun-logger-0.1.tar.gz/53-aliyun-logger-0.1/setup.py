from setuptools import setup, find_packages

setup(
    name='53-aliyun-logger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aliyun-log-python-sdk',
        'enum34'
    ],
    author='Your Name',
    author_email='your_email@example.com',
    description='Python package for Aliyun Logger',
    url='https://github.com/your_username/aliyun-logger',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
