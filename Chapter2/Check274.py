'''
Given a list of numbers in random order write a O(nlogn) time algorithm to find the 𝑘th
smallest number in the list. 
'''

random_list = [3,4,8,1,2,0]

def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]

print(kth_smallest(random_list, 3))

