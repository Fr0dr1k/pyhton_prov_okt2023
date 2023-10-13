#Fredrik Forsgard


def encrypt(list_of_rows):
    try:
        number_of_columns = len(list_of_rows[0])
    except IndexError:
        number_of_columns = 0

    resulting_text = ""
    for column in range(number_of_columns):
        for row in list_of_rows:
            resulting_text += row[column]

    return resulting_text


def test_encrypt():
    list_of_tests = [["ILOV", "EPRO", "GRAM", "MING"],
                     [],
                     ["", ""],
                     ["A"],
                     ["A", "B", "C"],
                     ["AB", "CD", "EF"],
                     ["ABCD"],
                     ["ABCDE", "FGHIJ"]]

    for test in list_of_tests:
        print(test, "blir", "\""+encrypt(test)+"\"")


def uppgift():
    test_encrypt()


if __name__ == '__main__':
    uppgift()
