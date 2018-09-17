# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 19:20:44 2018

@author: huangjin
"""
"""
翻牌问题
初始化牌面都向上
按顺序翻牌，每次翻牌会使得周围的一圈牌也翻转
输入：测试用例个数
输入：每个矩阵维度
输出：牌面向下的张数
"""
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N,M = [int(i) for i in input().split()]
        if N==1 and M==1:
            print(1)
        if N==1 and M!=1:
            print(M-2)
        if N!=1 and M==1:
            print(N-2)
        if M!=1 and N!=1:
            print(M*N-4-2*(M-2)-2*(N-2))
    