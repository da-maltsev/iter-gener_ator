from functools import wraps
import datetime

def log(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        date = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        with open('logs.txt', 'a') as f:
            f.write(f'{date}, функция {old_function.__name__}, аргументы {args} & {kwargs}, результат {result}\n')
        return result
    return new_function

def log_path(path):
    def log(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            date = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            with open(path, 'a') as f:
                f.write(f'{date}, функция {old_function.__name__}, аргументы {args} & {kwargs}, результат {result}\n')
            return result
        return new_function
    return log
