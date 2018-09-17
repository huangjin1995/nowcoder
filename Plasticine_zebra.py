# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 19:54:07 2018

@author: huangjin
"""
"""
输入：b,w构成的字符串
操作：可以多次以某点为分割点，反转，再拼接字符串，求最长的交替出现子串
输出：最大长度
无论操作多少次，总是由两段下标连续的串组成，
所以直接在原串后面接上原串，
求最长黑白相间连续串即可
"""
s1 = input()
s = s1+s1
# method 1 设置两个指针l,r
"""
l=r=0
res = 0
n =len(s)
while l<n and r<n-1:
    if s[r]!=s[r+1]:
        r=r+1
        if r-l==n-1:
            res = len(s1)
    else:
        res = max(r-l+1, res)
        l=r+1
        r=r+1
print(res)
"""
# method 2:对每个字符都求它的最大串长度
res = 1
for i in range(len(s)-1):
    l=1
    while i<len(s)-1 and s[i]!=s[i+1]:
        l = l+1
        i = i+1
    res = max(res, l)
if res > len(s1):
    res = len(s1)
print(res)