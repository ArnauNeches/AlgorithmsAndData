def binary_search(collection, item):
    first = 0 
    last = len(collection)
    found = False

    while first <= last and not found:
        midpoint = (first+last)//2

        if collection[midpoint] == item:
            found = True
        else:
            if collection[midpoint] > item:
                last = midpoint -1
            else:
                first = midpoint +1
    return found