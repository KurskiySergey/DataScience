from functools import reduce


def mul(a, b):
    return a*b


def list_mul(my_list):
    return reduce(mul, my_list)


if __name__ == "__main__":
    result = list_mul(my_list=[i for i in range(100, 1001) if i % 2 == 0])
    print(result)
