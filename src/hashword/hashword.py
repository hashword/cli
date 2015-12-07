import os
import hashlib
import pkg_resources
from appdirs import user_data_dir
import click
import pyperclip


def get_version():
    return pkg_resources.get_distribution('hashword').parsed_version.public


def get_user_services():
    data_dir = user_data_dir('hashword')
    try:
        with open(os.path.join(data_dir, 'keys.txt'), 'r') as key_file:
            keys = key_file.read()
        keys = keys.split(',')
        return [service.strip() for service in keys]
    except IOError:
        return []


def save_user_services(services):
    data_dir = user_data_dir('hashword')
    try:
        os.makedirs(data_dir)
    except OSError:
        pass
    services.sort()
    with open(os.path.join(data_dir, 'keys.txt'), 'w') as key_file:
        key_file.write(','.join(services) + '\n')


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
@click.option('--remove', '-r', default=False, is_flag=True,
                help='Remove a Service from the list.')
@list_services_option()
@click.version_option(message=get_version())
def cli(service, remove):
    if remove:
        success = remove_user_service(service)
        if success is True:
            click.echo('{} removed.'.format(service))
        else:
            keyfile = os.path.join(user_data_dir('hashword'), 'keys.txt')
            click.echo('{} not found in {}.'.format(service, keyfile))
        return
    user_services = get_user_services()
    if service not in user_services:
        add_user_service(service)

    master_password = click.prompt('Master Password', type=str, hide_input=True)
    hash_input = service + master_password
    password = sha256(hash_input)
    pyperclip.copy(password)
    click.echo('Password copied to clipboard.')
