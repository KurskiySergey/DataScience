if __name__ == "__main__":
    my_list = [7, 5, 3, 3, 2]
    min_el = min(my_list)
    print(my_list)
    while True:
        number = int(input("value (-1 to exit): "))
        if number == -1:
            break

        if number < min_el:
            my_list.append(number)
            min_el = number
        else:
            for i, el in enumerate(my_list):
                if number > el:
                    my_list.insert(i, number)
                    break
        print(my_list)
