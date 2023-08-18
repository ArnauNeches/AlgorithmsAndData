

def reverse_list(my_list):
    if len(my_list) == 0:
        return []
    else:
        return [my_list[-1]] + reverse_list(my_list[:-1])
    
if __name__ == "__main__":
    alist = [1, 2, 3, "dog", 5]
    print(reverse_list(alist))