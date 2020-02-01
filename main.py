import logging.config
from lgtm import core


logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'basicFormatter': {
            'format': '%(asctime)s %(levelname)-6s %(message)s'
        }
    },
    'handlers': {
        'basicHandlers': {
            'class': 'logging.StreamHandler',
            'formatter': 'basicFormatter',
            'level': logging.DEBUG,
        }
    },
    'root': {
        'handlers': ['basicHandlers'],
        'level': logging.WARNING,
    },
    'loggers': {
        'basicLogger': {
            'handlers': ['basicHandlers'],
            'level': logging.DEBUG,
            'propagate': 0,
        }
    }
})

logger = logging.getLogger('basicLogger')


if __name__ == '__main__':
    core.cli()