import ast
import os
import re
from setuptools import setup, find_packages


THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def get_version():
    _version_re = re.compile(r'VERSION\s+=\s+(.*)')
    source_file = os.path.join(THIS_DIR, 'src', 'hashword', 'hashword.py')
    with open(source_file, 'rb') as f:
        version = str(ast.literal_eval(_version_re.search(
            f.read().decode('utf-8')).group(1)))
    return version


setup(
    name='hashword',
    version=get_version(),
    packages=find_packages(where='src'),
    package_dir = {'':'src'},
    install_requires=[
        'appdirs>1',
        'click>6',
        'pyperclip>1',
    ],
    entry_points='''
        [console_scripts]
        hashword=src.hashword.hashword:cli
    ''',
)
