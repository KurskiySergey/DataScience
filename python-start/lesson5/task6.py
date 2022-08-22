import re
from config import full_filename

if __name__ == "__main__":
    filename = "task6.txt"

    pattern = "\d+"
    re_exp = re.compile(pattern=pattern)
    result = {}
    with open(full_filename(filename), "r", encoding="utf-8") as file:
        for line in file:
            name = line.split(":")[0]
            values = map(int, re_exp.findall(line))
            result[name] = sum(values)

    print(result)
