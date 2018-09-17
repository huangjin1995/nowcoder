# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:55:23 2018

@author: huangjin
"""
# 完成任务最小代价
"""
输入：3个整数
输出：最小代价
"""
if __name__=='__main__':
    input_list = [int(i) for i in input().split()]
    input_list.sort()
    input_list.reverse()
    res = input_list[0]-input_list[1]
    res = res + input_list[1]-input_list[2]
    print(res)