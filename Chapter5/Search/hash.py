def hash(s, size):
    sum = 0
    for pos in range(len(s)):
        sum += ord(s[pos])
    
    return sum % size
