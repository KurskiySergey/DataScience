
if __name__ == "__main__":
    len_of_array = int(input("Length of array: "))
    array = [int(input()) for _ in range(len_of_array)]
    len_of_array = len_of_array - 1 if len_of_array % 2 != 0 else len_of_array + 1

    print(f"Before changing = {array}")
    for i in range(1, len_of_array, 2):
        array[i-1], array[i] = array[i], array[i-1]
    print(f"After changing = {array}")
