'''
Given two sorted arrays of size m and n of distinct elements. Given a value x. 
The problem is to count all pairs from both arrays whose sum is equal to x.
Note: The pair has an element from each array.

Examples:

Input : arr1[] = {1, 3, 5, 7}
        arr2[] = {2, 3, 5, 8}
        x = 10

Output : 2
The pairs are:
(5, 5) and (7, 3)

Input : arr1[] = {1, 2, 3, 4, 5, 7, 11} 
        arr2[] = {2, 3, 4, 5, 6, 8, 12} 
        x = 9

Output : 5
'''

import array

def countsumnum(list1, list2, sumnum):
    count = 0
    array1 = array.array('i', list1)
    array2 = array.array('i', list2)
    for i in range(len(array1)):
        for j in range(len(array2)-1, -1, -1):
            if array1[i] + array2[j] >= sumnum:
                if array1[i] + array2[j] == sumnum:
                    count += 1
                    array2.pop(j)
            else:
                break
    print(count)
    
if __name__=='__main__':
    list1 = [1, 2, 3, 4, 5, 7, 11]
    list2 = [2, 3, 4, 5, 6, 8, 12]
    sumnum = 9
    countsumnum(list1, list2, sumnum)
