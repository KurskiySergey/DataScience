if __name__ == "__main__":
    array = [1, 2.5, "hello", ["1", "world", {}], {1: "hello", "2": 3}]
    print(array)
    for el in array:
        print(type(el))