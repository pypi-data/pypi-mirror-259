from setuptools import setup, find_packages

setup(
    name='sstpy',
    version='0.1.0',
    author='HankyZhao',
    author_email='zhq980115@gmail.com',
    description='A python wrapper project for sstable',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://codeup.aliyun.com/64ddb0a87f62ff9b3d23ca15/py_sstable',
    package_dir={'core': 'core', 'test': 'test', 'format': 'format'},
    packages=['core', 'test', 'format'],  # 手动指定包目录
    package_data={
        # 如果lib文件与特定包关联，可以这样指定
        # 'package_name': ['lib/some_library.so']
    },
    data_files=[
        # 将lib目录下的.so文件放在安装目录的lib下
        ('lib', ['lib/libsstable_internal.so']),
    ],
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
