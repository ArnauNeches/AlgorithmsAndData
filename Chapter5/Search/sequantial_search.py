def sequential_search(collection, item):
    pos = 0
    found = False

    while pos < len(collection) and not found:
        if collection[pos] == item:
            found = True
        else:
            pos += 1
    
    return found

