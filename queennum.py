'''
Number of cells a queen can move with obstacles on the chessborad

source:  http://www.geeksforgeeks.org/?p=149866
'''
from numpy import zeros

def initarray(n, list1, list2):
    arr = zeros((n,n), dtype=int)
    set1 = zip(list1, list2)
    for i in set1:
        arr[i] = 1
    return arr

def check(arr, x, y, xx, yy, n):
    count = 0
    for i in range(n):
        if -1< x + xx <n and -1< y + yy < n and arr[x+xx][y+yy] !=1:
            count += 1
            x += xx
            y += yy
        else:
            break
    return count

def numberofpositon(n, list1, list2, x, y):
    arr = initarray(n, list1, list2)
    count1 = check(arr, x, y, 1, 0, n)
    count1 += check(arr, x, y, 0, 1, n)
    count1 += check(arr, x, y, 0, -1, n)
    count1 += check(arr, x, y, -1, 0, n)
    count1 += check(arr, x, y, 1, 1, n)
    count1 += check(arr, x, y, -1, -1, n)
    count1 += check(arr, x, y, 1, -1, n)
    count1 += check(arr, x, y, -1, 1, n)
    return count1
print(initarray(8, [3,5], [4,7]))
print(numberofpositon(8, [3,5], [4,7], 3, 3))
