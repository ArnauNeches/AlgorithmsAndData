#This function will recive a string and return it reversed using recursion

def reverse_str(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_str(s[:-1])

if __name__ == "__main__":
    print(reverse_str("Hello World"))