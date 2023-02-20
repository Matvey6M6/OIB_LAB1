ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def read_file(filename):
    with open(filename, "r", encoding='utf-8') as file:
        return file.read()


def write_file(filename, text):
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)


def check(key):
    for sym in ALPHABET:
        if(key.count(sym) != 1):
            return False
    return True


if "__main__" == __name__:
    key = input("Enter the key (33 char.): ").lower()
    if(len(key) != 33 and not check(key)):
        print("incorrectly key!")
        exit(0)

    text = read_file("text1.txt").lower()

    for i, sym in enumerate(ALPHABET):
        text = text.replace(sym, key[i])

    write_file("text2.txt", text)