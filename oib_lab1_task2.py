def read_file(filename):
    with open(filename, "r", encoding='utf-8') as file:
        return file.read()


def write_file(filename, text):
    with open(filename, "w", encoding='utf-8') as file:
        file.write(text)

def unique_sym(encrypted):
    list_sym = list()

    for sym in encrypted:
        if(sym not in list_sym):
            list_sym.append(sym)
            count_sym = encrypted.count(sym)
            print(sym, count_sym, count_sym / len(encrypted), sep="   ")


if "__main__" == __name__:
    encrypted = read_file("text1_task2.txt")
    unique_sym(encrypted)

    encrypted = encrypted.replace(" ", "ъ")
    encrypted = encrypted.replace("c", " ")
    encrypted = encrypted.replace("А", "о")
    encrypted = encrypted.replace("Х", "и")
    encrypted = encrypted.replace("8", "е")
    encrypted = encrypted.replace("М", "т")
    encrypted = encrypted.replace("r", "н")
    encrypted = encrypted.replace("Л", "с")
    encrypted = encrypted.replace("О", "а")
    encrypted = encrypted.replace("2", "к")
    encrypted = encrypted.replace("b", "я")
    encrypted = encrypted.replace("К", "р")
    encrypted = encrypted.replace("Е", "м")
    encrypted = encrypted.replace("Д", "л")
    encrypted = encrypted.replace("Б", "п")
    encrypted = encrypted.replace("Р", "в")
    encrypted = encrypted.replace("7", "д")
    encrypted = encrypted.replace("4", "ь")
    encrypted = encrypted.replace("t", "у")
    encrypted = encrypted.replace("1", "й")
    encrypted = encrypted.replace("<", "ч")
    encrypted = encrypted.replace("Ф", "з")
    encrypted = encrypted.replace("У", "ж")
    encrypted = encrypted.replace("5", "э")
    encrypted = encrypted.replace(">", "г")
    encrypted = encrypted.replace("Ч", "ц")
    encrypted = encrypted.replace("?", ".")
    encrypted = encrypted.replace("И", "ф")
    encrypted = encrypted.replace("П", "б")
    encrypted = encrypted.replace("Й", "х")
    encrypted = encrypted.replace("Ь", "щ")
    encrypted = encrypted.replace("Ы", "ш")

    
    write_file("text2_task2.txt", encrypted)