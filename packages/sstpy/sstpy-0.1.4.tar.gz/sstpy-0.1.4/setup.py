from setuptools import setup, find_packages

setup(
    name='sstpy',
    version='0.1.4',
    author='HankyZhao',
    author_email='zhq980115@gmail.com',
    description='A python wrapper project for sstable',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://codeup.aliyun.com/64ddb0a87f62ff9b3d23ca15/py_sstable',
    packages=find_packages(),
    package_data={
        # 确保 'lib/libsstable_internal.so' 被包含
        '': ['lib/libsstable_internal.so'],
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
