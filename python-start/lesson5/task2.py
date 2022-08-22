from config import full_filename

if __name__ == "__main__":
    filename = "task2.txt"

    with open(full_filename(filename), "r") as f:
        lines = f.readlines()
        word_counter_list = [len(line.split(" ")) for line in lines]

    print(f"lines count: {len(lines)}")
    print(f"word counter per line: {word_counter_list}")
