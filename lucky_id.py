# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 14:15:41 2018

@author: huangjin
"""
"""
输入：6位数字字符串
幸运数：前三位和后三位和相等
每次可以改变其中一个数字的大小
输出：最小的改变次数使得输入为幸运数
"""
if __name__=='__main__':
    input_list = input()
    left = sum(int(i) for i in input_list[:3])
    right = sum(int(i) for i in input_list[3:])
    diff = left-right
    if diff == 0:
        print(0)
    else:
        res = 0
        num = [int(i) for i in input_list]
        if diff<0:
            tem = [9-i for i in num[:3]]+num[3:]
            while diff<0:
                res+=1
                diff = diff+max(tem)
                tem[tem.index(max(tem))]=0
            print(res)
        else:
            tem = num[:3] + [9-i for i in num[3:]]
            while diff>0:
                res+=1
                diff = diff-max(tem)
                tem[tem.index(max(tem))]=0
            print(res)
    