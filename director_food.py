# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:30:17 2018

@author: huangjin
"""
# 爱奇艺：局长的食物
"""
输入：食物种类,天数,需要查询的食物类别
输入：对食物的操作
输出：食物P的数量rank
"""
if __name__=='__main__':
    line_1 = input().split()
    N,M,P=int(line_1[0]), int(line_1[1]), int(line_1[2])
    line_2 = input().split()
    count = [int(i) for i in line_2]
    for i in range(M):
        action, food_name = input().split()
        food_name = int(food_name)
        if action=='A':
            count[food_name-1] = count[food_name-1]+1
        if action=='B':
            count[food_name-1] = count[food_name-1]-1
    tmp = sorted(count)
    tmp.reverse()
    """  
    for i in range(len(tmp)):
        if count[P-1]==tmp[i]:
            res = i+1
            print(res)
            break
    """
    res = tmp.index(count[P-1])+1
    print(res)
            
        