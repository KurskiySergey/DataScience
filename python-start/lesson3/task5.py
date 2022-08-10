def sum_iterator():
    result = 0
    while True:
        string = input("string of numbers (Enter to exit or !): ")
        if string == "":
            break
        try:
            result += sum(map(int, string.split(" ")))
        except (ValueError, TypeError):
            if "!" in string:
                try:
                    result += sum(map(int, string.split("!")[0].split(" ")[:-1]))
                    break
                except (TypeError, ValueError):
                    break
        finally:
            print(f"total sum is: {result}\n")


if __name__ == "__main__":
    sum_iterator()
