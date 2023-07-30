#Self check 2.2.1

'''
Write two Python functions to find the minimum number in a list. The first function should
compare each number to every other number on the list. 𝑂(𝑛^2). The second function should be
linear 𝑂(𝑛).
'''

list_objective = [1,2,3,4,5,6]

def min_quadratic(numbers):
    res = numbers[0]
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] < res:
                res = numbers[j]
    return res

def min_lineal(numbers):
    res = numbers[0]
    for num in numbers:
        if num < res:
            res = num
    return res
        


print(min_quadratic(list_objective)) 
print(min_lineal(list_objective))           

