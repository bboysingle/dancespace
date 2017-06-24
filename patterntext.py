'''
Suppose we have two Strings :- Pattern and Text
pattern: consisting of unique characters
text: consisting of any length
We need to find the number of patterns that can be 
obtained from text removing each and every occurrence of Pattern in the Text.
Input : 
Pattern : ABC
Text : ABABCABCC
Output :
3
'''

patternx = 'ABC'
textA = 'ABABCABCC'
count = 0
while textA.find(patternx) != -1:
    posit = textA.find(patternx)
    listA = list(textA)
    listTemp = listA[:posit] + listA[posit + len(patternx):]
    textA = "".join(listTemp)
    count +=1
print(count)
