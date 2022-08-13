from task5 import list_mul


def fact(n):
    for value in range(n+1):
        yield list_mul([i for i in range(1, value+1)]) if value != 0 else 1


def fact_2(n):
    start_value = 1
    for value in range(n+1):
        start_value *= value if value != 0 else 1
        yield start_value


if __name__ == "__main__":

    for el in fact(n=5):
        print(el)

    print()
    for el in fact_2(n=5):
        print(el)
