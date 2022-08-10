
def my_func(a, b, c):
    try:
        result = max([a+b, a+c, b+c])
    except (ValueError, TypeError):
        print("Exception")
        result = 0
    return result


if __name__ == "__main__":
    print(my_func(10, -2, 30))
