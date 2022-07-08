from datetime import datetime
from functools import wraps


def logger(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        with open('log.txt', 'a', encoding='utf-8') as file:
            log = [f'Дата и время вызова функции: {start_time}\n',
                   f'Имя функции: {func.__name__}\n',
                   f'Аргументы функции: {args, *kwargs}\n',
                   f'Возвращаемое значение: {result}\n'
                   '\n']
            file.writelines(log)
        return result
    return inner_func


def logger_params(file_name):
    def decorator(func):
        @wraps(func)
        def inner_func(*args, **kwargs):
            start_time = datetime.now()
            result = func(*args, **kwargs)
            with open(file_name, 'a', encoding='utf-8') as file:
                log = [f'Дата и время вызова функции: {start_time}\n',
                       f'Имя функции: {func.__name__}\n',
                       f'Аргументы функции: {args, kwargs}\n',
                       f'Возвращаемое значение: {result}\n'
                       '\n']
                file.writelines(log)
            return result
        return inner_func
    return decorator
