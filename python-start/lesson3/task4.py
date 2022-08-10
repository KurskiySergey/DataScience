def my_func(a, b):
    if a > 0 and b < 0:
        return 1 / a ** abs(b)
    else:
        print("a > 0 and b < 0")
        return None


def while_my_func(a, b):
    if a > 0 and b < 0:
        result = 1
        while abs(b) > 0:
            result *= a
            b += 1
        return 1 / result
    else:
        print("a > 0 and b < 0")
        return None


if __name__ == "__main__":
    print(my_func(3, -2), while_my_func(3, -2))
