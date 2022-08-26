from pprint import pprint

if __name__ == "__main__":
    user_string = input("Write your sentence: ")

    for i, word in enumerate(user_string.split()):
        print(f"{i}: {word[:10]}")
