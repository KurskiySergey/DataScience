def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("zero division")
        result = None

    return result


if __name__ == "__main__":
    a = int(input("a value: "))
    b = int(input("b value: "))
    print(division(a, b))
