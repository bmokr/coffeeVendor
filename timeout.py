from threading import Thread  # https://stackoverflow.com/questions/21827874/timeout-a-function-windows
import functools
# library and function imported from:
# https://docs.python.org/3/library/threading.html#threading.Thread.join
# timeout is used for service task that was meant to last no longer than some period of time


def timeout(seconds_before_timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, seconds_before_timeout))]

            def new_func():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as E:
                    res[0] = E
            t = Thread(target=new_func)
            t.daemon = True
            try:
                t.start()
                t.join(seconds_before_timeout)
            except Exception as e:
                print('error starting thread')
                raise e
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco
