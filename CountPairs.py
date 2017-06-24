'''
find number of possible pairs (a, b) such that GCD(a, b) is equal 
to given G and LCM (a, b) such that LCM(a, b) is equal to given L.
Input : G = 2, L = 12
Output : 4
Explanation : There are 4 possible pairs :
(2, 12), (4, 6), (6, 4), (12, 2)
'''

def countpairs(G, L):
    count = 0
    multy = G*L
    list1 = list(range(G, L + 1))
    for i in list1:
        if multy/i in list1 and gcd(i, multy/i) == G:
            count += 1
            print("(%d, %d)" % (i, multy/i))
    print("sum of the pairs is: %d" % count)        
def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)
           
countpairs(2, 24)

