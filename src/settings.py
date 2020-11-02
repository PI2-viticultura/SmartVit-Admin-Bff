import os


def load_configuration():
    config = dict()
    config['host'] = os.environ.get('HOST_GATEWAY', 'localhost')
    config['port'] = int(os.environ.get('HTTP_PORT', '8080'))
    config['reload'] = os.environ.get('DEBUG', True)

    return config
