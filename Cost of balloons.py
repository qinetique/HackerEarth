#Author: Tonmoy Mondal
#URL: https://qinetique.github.io
#Problem: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/

cs = int(input())
for i in range(cs):

    a, b = map(int, input().split())
    n = int(input())
    costofbal = 0
    l = min(a,b)
    m = max(a,b)
    a_total01 = 0
    a_total02 = 0
    for j in range(n):
        x, y = map(int, input().split())
        a_total01 += x
        a_total02 += y
    if a_total01 >= a_total02:
        costofbal += a_total01 * l
        costofbal += a_total02 * m
    else:
        costofbal += a_total02 * l
        costofbal += a_total01 * m
    print(costofbal)