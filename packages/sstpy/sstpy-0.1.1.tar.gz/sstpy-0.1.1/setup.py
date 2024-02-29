from setuptools import setup, find_packages

setup(
    name='sstpy',
    version='0.1.1',
    author='HankyZhao',
    author_email='zhq980115@gmail.com',
    description='A python wrapper project for sstable',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://codeup.aliyun.com/64ddb0a87f62ff9b3d23ca15/py_sstable',
    packages=find_packages(),  # 自动找到所有包
    package_data={
        # 如果您有特定包相关的数据文件
        'sstpy': ['lib/libsstable_internal.so'],
    },
    include_package_data=True,  # 包括MANIFEST.in中指定的所有文件
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
