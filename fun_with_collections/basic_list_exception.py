def make_list():
    a = []
    i = 0
    while i < 3:
        a.insert(i, int(get_input()))
        if a[i] > 50 or a[i] < 1:
            raise ValueError
        i = i + 1

    return a


def get_input():
    return input("Enter a number: ")


if __name__ == '__main__':
    list = make_list()
    for i in range(0, len(list)):
        print(list[i])

