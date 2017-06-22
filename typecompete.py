#coding=utf-8
'''
某学校进行打字比赛，比赛主要考查选手在规定时间内正确输入的字数。
但问题是，如何确定每一个输入的字是否是正确的（即是否与原稿相同），因为完全存在选手错字、漏字和增字的情况，
如：原稿为“abcde”,打字内容为“abece”.比较可靠的办法是计算打字内容与原稿的最大相似子序列的长度，
所谓最大相似子序列即两者相等的子序列种最大的那个，如前面例子中两者最大相似子序列的长度为“abce”，
长度为4，请设计程序计算两个字符串的最大相似子序列的长度！
'''
str1="interneabct"
str2="returnabc"
l1=list(str1)
l2=list(str2)
i=0
j=0
k=0
listres=[0]
count=0
while i <len(l2):
    count=0
    l1=list(str1)
    j=j+i
    while j < len(l2):
        if l2[j] in l1:
            indx = l1.index(l2[j])
            l1=l1[indx+1:]
            #print(i,j,l1)
            count=count+1
        j=j+1
    listres.append(count)
    i=i+1
    j=0
print(max(listres))
