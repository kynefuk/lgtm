from functools import wraps


def log_info_deco(logger):
    def _log_info_deco(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            logger.info({
                'action': f.__qualname__,
                'kwargs': kwargs,
                'status': 'run'
            })
            v = f(*args, *kwargs)
            logger.info({
                'action': f.__qualname__,
                'kwargs': kwargs,
                'status': 'success'
            })
            # 戻り値がある関数のためreturnする必要がある
            return v
        return wrapper
    return _log_info_deco
