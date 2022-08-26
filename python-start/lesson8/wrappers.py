import sys
import traceback


def try_exception(exception):

    def wrapper(func):

        def data(*args, **kwargs):

            try:
                return func(*args, **kwargs)
            except exception:
                print(traceback.format_exc().split("\n")[-2])
                sys.exit(-1)

        return data

    return wrapper


def try_warning(exception):
    def wrapper(func):

        def data(*args, **kwargs):

            try:
                return func(*args, **kwargs)
            except exception:
                print(traceback.format_exc().split("\n")[-2])

        return data

    return wrapper
