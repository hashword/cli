from setuptools import setup, find_packages


setup(
    name='hashword',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
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
