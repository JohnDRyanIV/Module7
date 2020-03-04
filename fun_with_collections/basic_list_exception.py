def make_list():
    a = []
    i = 0
    while i < 3:
        try:
            a.insert(i, int(get_input()))
            i = i + 1
        except ValueError:
            raise ValueError
            print("Incorrect input. Try again")
    return a


def get_input():
    return input("Enter a number: ")


if __name__ == '__main__':
    list = make_list()
    for i in range(0, len(list)):
        print(list[i])

