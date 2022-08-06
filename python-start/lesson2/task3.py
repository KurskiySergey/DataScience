if __name__ == "__main__":
    seasons = [
        "winter",
        "spring",
        "summer",
        "autumn",
    ]

    mounth = {
        i if i != 0 else 12: seasons[i // 3] for i in range(12)
    }

    print(mounth)

    mounth_value = int(input("Write mounth number "))

    print(mounth.get(mounth_value))
