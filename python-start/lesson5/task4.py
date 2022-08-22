from config import full_filename
NUMBER_LIST = ["Один", "Два", "Три", "Четыре"]
NUMBER_DICTIONARY = {f"{i+1}": word for i, word in enumerate(NUMBER_LIST)}

if __name__ == "__main__":
    filename = "task4.txt"
    result_filename = "task4_rus.txt"

    with open(full_filename(filename), "r", encoding="utf-8") as file:
        with open(full_filename(result_filename), "w", encoding="utf-8") as res_file:
            while True:
                line = file.readline()

                if line == "":
                    break
                value = line.strip().split(' — ')[1]
                result_str = f"{NUMBER_DICTIONARY.get(value)} — {value}\n"
                res_file.write(result_str)
                print("#####", f"file string: {line}", f"result string: {result_str}", sep="\n")
