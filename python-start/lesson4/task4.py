from collections import Counter

if __name__ == "__main__":
    test_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [key for key, value in Counter(test_list).items() if value == 1]
    print(result)
