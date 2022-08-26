
if __name__ == "__main__":
    test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [element for i, element in enumerate(test_list) if element > test_list[i-1] and i > 0]
    print(result)
