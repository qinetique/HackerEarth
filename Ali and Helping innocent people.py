# Author: Tonmoy Mondal
# URL: https://qinetique.github.io
# Problem: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cartag-948c2b02/

# one test case is error;
# lets approach another style/ method

tag = input()
vowels = ["A", "E", "I", "O", "U", "Y"]
en1 = int(tag[0]) + int(tag[1])
en2 = int(tag[3]) + int(tag[4])
en3 = int(tag[4]) + int(tag[5])
en4 = int(tag[7]) + int(tag[8])

if tag[2] in vowels:
    print("invalid")
elif en1 % 2 == 0 and en2 % 2 == 0 and en3 % 2 == 0 and en4 % 2 == 0:
    print("valid")
else:
    print("invalid")