import os
import hashlib
from appdirs import user_data_dir
import click
import pyperclip


VERSION = '1.0.0'


def get_user_services():
    data_dir = user_data_dir('hashword')
    try:
        with open(os.path.join(data_dir, 'keys.txt'), 'r') as key_file:
            keys = key_file.read().split('\n')
        return keys
    except FileNotFoundError:
        return []


def save_user_services(services):
    data_dir = user_data_dir('hashword')
    try:
        os.makedirs(data_dir)
    except FileExistsError:
        pass
    with open(os.path.join(data_dir, 'keys.txt'), 'w') as key_file:
        for service in services:
            key_file.write(service + '\n')


def add_user_service(service):
    services = get_user_services()
    services.append(service)
    services.sort()
    save_user_services(services)


def remove_user_service(service):
    services = get_user_services()
    services.remove(service)
    save_user_services(services)


def sha256(text):
    text = text.encode('utf-8')
    return hashlib.sha256(text).hexdigest()


def list_services_option(*param_decls, **attrs):
    def decorator(f):
        def callback(ctx, param, value):
            if not value or ctx.resilient_parsing:
                return
            services = get_user_services()
            for service in services:
                click.echo(service)
            ctx.exit()

        attrs.setdefault('is_flag', True)
        attrs.setdefault('expose_value', False)
        attrs.setdefault('is_eager', True)
        attrs.setdefault('help', 'List Services and exit.')
        attrs['callback'] = callback
        return click.decorators.option(
            *(param_decls or ('--list', '-l')), **attrs)(f)
    return decorator


@click.command()
@click.argument('service')
@click.option('--remove', '-r', default=False, is_flag=True)
@list_services_option()
@click.version_option(message=VERSION)
def cli(service, remove):
    if remove:
        remove_user_service(service)
        click.echo('{} removed.'.format(service))
        return
    user_services = get_user_services()
    if service not in user_services:
        add_user_service(service)

    master_password = click.prompt('Master Password', type=str, hide_input=True)
    hash_input = service + master_password
    password = sha256(hash_input)
    pyperclip.copy(password)
    click.echo('Password copied to clipboard.')
