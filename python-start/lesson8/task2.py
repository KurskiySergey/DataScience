from exeptions import ZeroError
from wrappers import try_warning


@try_warning(ZeroError)
def division(a, b):
    if b == 0:
        raise ZeroError(message="Division by 0 is forbidden")
    return a / b


if __name__ == "__main__":
    print(division(10, 0))
