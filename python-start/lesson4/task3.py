
if __name__ == "__main__":
    result_1 = [element for element in range(20, 240) if element % 20 == 0 or element % 21 == 0]  # not include 240
    result_2 = [element for element in range(20, 241) if element % 20 == 0 or element % 21 == 0]  # include 240
    print(result_1, result_2, sep="\n")
