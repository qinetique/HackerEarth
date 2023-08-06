#Author: Tonmoy Mondal
#URL: https://qinetique.github.io
#Problem: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/divisible-or-not-81b86ad7/

N = int(input())
fuckin_array = list(map(int, input().split()))
div = fuckin_array[N - 1]
if div % 10 == 0:
    print("Yes")
else:
    print("No")