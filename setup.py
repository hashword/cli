from setuptools import setup, find_packages


setup(
    name='hashword',
    url='https://github.com/hashword/cli',
    author='Cody Scott',
    author_email='cody.j.b.scott@gmail.com',
    description='A console program to concatentate two words to create passwords.',
    license='MIT',
    keywords='hashword password manager',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(where='src'),
    package_dir = {'':'src'},
    install_requires=[
        'appdirs>1',
        'click>6',
        'pyperclip>1',
        'scrypt>0',
    ],
    entry_points='''
        [console_scripts]
        hashword=hashword.hashword:cli
    ''',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
