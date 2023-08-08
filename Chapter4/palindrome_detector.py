#Palindrome detector using recursion

def palindrome(s: str) -> bool:
    if len(s) <= 2:
        return s[0] == s[-1]
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])

if __name__ == "__main__":
    print(palindrome("kayyak"))
    print(palindrome("hola"))