from task1 import ask_params_from_user


if __name__ == "__main__":
    repeat_value = 3  # n + nn + nnn + ... + n*repeat_value
    number = ask_params_from_user(type_of_param="int")
    # n + nn + nnn = n + 10*n + n + 100*n + 10*n + n = 3 * n + 2 * 10*n + 1 * 100*n
    sum_array = [number * (repeat_value - i) * pow(10, i) for i in range(repeat_value)]
    result = sum(sum_array)
    print(result)

