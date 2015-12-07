from copy import copy
import os
from appdirs import user_data_dir
from click.testing import CliRunner
import pyperclip
from hashword.hashword import (add_user_service, cli, get_user_services,
                                save_user_services, sha256)


def test_get_user_services():
    services = ['one', 'two', 'three']
    save_user_services(services)
    expected = copy(services)
    expected.sort()
    assert get_user_services() == expected


def test_add_user_service():
    services = ['one', 'two', 'three']
    save_user_services(services)
    add_user_service('four')
    expected = copy(services)
    expected.append('four')
    expected.sort()
    assert get_user_services() == expected


def test_save_user_services():
    services = ['one', 'two', 'three']
    save_user_services(services)
    data_dir = user_data_dir('hashword')
    with open(os.path.join(data_dir, 'keys.txt'), 'r') as key_file:
        contents = key_file.read()
    assert contents == ','.join(sorted(services)) + '\n'


def test_get_password():
    runner = CliRunner()
    result = runner.invoke(cli, args='service', input='masterpassword\n')
    print(result)
    print (result.exception)
    assert not result.exception
    assert result.output == 'Foo: wau wau\nfoo=wau wau\n'
    assert pyperclip.paste() == sha256('testmasterpassword')
