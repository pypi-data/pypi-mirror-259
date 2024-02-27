from setuptools import setup, find_packages

setup(
    name='x01replace',
    version='1.0.1',
    author='tangjicheng',
    author_email='tangjch15@gmail.com',
    description='A tool to replace \\x01 with |',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'x01replace=x01replace:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
