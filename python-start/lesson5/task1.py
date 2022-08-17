from config import full_filename, DEFAULT_FILE_NAME


def write_to_file(filename):
    with open(full_filename(filename), "w") as f:
        while True:
            input_str = input("Write new line (Enter to stop writing): ")
            if input_str == "":
                break
            f.write(f"{input_str}\n")


if __name__ == "__main__":
    filename = input("Enter filename to write( test.txt by default) : ")
    if filename == "":
        filename = DEFAULT_FILE_NAME
    write_to_file(filename=filename)