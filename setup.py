import ast
import re
from setuptools import setup


def get_version():
    _version_re = re.compile(r'VERSION\s+=\s+(.*)')
    with open('hashword.py', 'rb') as f:
        version = str(ast.literal_eval(_version_re.search(
            f.read().decode('utf-8')).group(1)))
    return version


setup(
    name='hashword',
    version=get_version(),
    py_modules=['hashword'],
    install_requires=[
        'appdirs>1',
        'click>6',
        'pyperclip>1',
    ],
    entry_points='''
        [console_scripts]
        hashword=hashword:cli
    ''',
)
