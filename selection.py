# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:25:50 2021
"""

string = '이번 주 수요일 부터해서 (2박)/(이 박) (3일)/(삼 일)이요.'

def selection(string):
    # 여기에서 앞의 것만 선택하자
    while True:
        if '/' not in string:
            break
        else:
            for i in range(len(string)):
                if string[i]=='/':
                    check3 = None
                    for k in range(i,len(string)):
                        if string[k]==')':
                            check3 = k
                            break

                    check1=None
                    check2=None
                    for j in range(i,-1,-1):
                        print(string[j])
                        if string[j]==')':
                            check2=j
                        elif string[j]=='(':
                            check1=j


                    answer = string[check1+1:check2]
                    break
            string = string[:check1]+answer+string[check3+1:]
    return string
