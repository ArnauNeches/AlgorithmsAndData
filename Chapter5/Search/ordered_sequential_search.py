def ordered_sequential_search(collection, item):
    pos = 0
    found = False
    stop = False

    while pos < len(collection) and not found and not stop:
        if collection[pos] == item:
            found = True
        else:
            if collection[pos] > item:
                stop = True
            else:
                pos += 1
    return found

            