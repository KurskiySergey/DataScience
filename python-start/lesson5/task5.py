from config import full_filename
from random import randint
MIN_VALUE = 0
MAX_VALUE = 1000
AMOUNT = 10

if __name__ == "__main__":
    filename = "task5.txt"

    # after each start new values will be added to the end
    with open(full_filename(filename), "r+", encoding="utf-8") as file:
        file.write(" ".join([str(randint(MIN_VALUE, MAX_VALUE)) for _ in range(AMOUNT)]))

        values = map(int, file.readline().strip().split(" "))
        print(f"Sun of values in file = {sum(values)}")
