'''
Given a number n, we need to find the nth number whose each digit 
is a prime number i.e 2, 3, 5, 7, 22, 23, 25, 27,32,33,...
In other words you have to find nth number of this sequence. 2, 3, 5, 7, 22, 23, 25, 27,32,33,...
Given that the nth number such found will be less then equal to 10^18
Examples:

Input  : 10
Output : 33
         2, 3, 5, 7, 22, 23, 25, 
         27, 32, 33

Input: 21
Output: 222
'''

def findlen(n):
    i = 0
    while True:
        if 4*(4**i - 1)/3 > n:
            return i
        else:
            i += 1

def findnthnum(n):
    numlen = findlen(n)
    less_count = 4*(4**(numlen-1) - 1)/3
    for i in range(numlen):
        for j in range(4):
            if (j+1)*4**(numlen-1-i) + less_count >= n:
                less_count = j*4**(numlen-1-i) + less_count
                if j==0:
                    print('2', end="")
                if j==1: 
                    print('3', end="")
                if j==2:
                    print('5', end="")
                if j==3:
                    print('7', end="")
                break
                
findnthnum(10)



