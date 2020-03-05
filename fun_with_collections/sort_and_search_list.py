def sort_list():  # Sort the list
    pass


    # Not returning the list because it's passed to sort_list as a reference, thus any changes made here will be
    # reflected in the original list.


def search_list(a, item):  # Return the index of the object in the list
    """
    :param a: list containing the item being searched for
    :param item: item the list is being searched for
    :return: index of object if found, -1 otherwise
    """
    for i in range(0, len(a)):
        try:
            if a[i] == item:
                return i
        except TypeError:
            pass
    return -1


if __name__ == '__main__':
    pass

