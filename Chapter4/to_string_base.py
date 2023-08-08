#Function to convert from decimal to any base (hexadecimal) using recursion

def to_string(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_string(n//base, base)+convert_string[n%base]
    
if __name__ == "__main__":
    print(to_string(435, 2))