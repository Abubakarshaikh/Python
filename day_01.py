# Q:1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# .....
# l =[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# print(','.join(l))

# Q:2. Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# ......
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x-1)

# x = int(input())
# print(fact(x))

# Q:3. with a given integral number n, write a program to generate a dictionary
#  that contains (i, i*i) such that is an integral number between 1 and n (both included). 
#  and then the program should print the dictionary.
# ........
n=int(input())
d=dict()
8
for i in range(1,n+1):
    # indexing 8
    d[i] = i*i
print(d)