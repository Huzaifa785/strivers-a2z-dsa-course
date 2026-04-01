import sys
input = sys.stdin.readline


# ======================================================
# 1. print numbers 1 to 5 using for loop
#    expected output:
#    1 2 3 4 5
# ======================================================
# for i in range(1, 6):
#     print(i, end=" ")

# ======================================================
# 2. print numbers 5 to 1 using for loop (countdown)
#    expected output:
#    5 4 3 2 1
# ======================================================
# for i in range(5, 0, -1):
#     print(i, end=" ")

# ======================================================
# 3. print numbers 1 to n using for loop (n from input)
#    input.txt: 7
#    expected output:
#    1 2 3 4 5 6 7
# ======================================================
# n = int(input())
# for i in range(1, n+1):
#     print(i, end=" ")


# ======================================================
# 4. print multiplication table of n (n from input)
#    input.txt: 3
#    expected output:
#    3 x 1 = 3
#    3 x 2 = 6
#    ...
#    3 x 10 = 30
# ======================================================
# n = int(input())
# for i in range(1, 11):
#     print(n, "X", i, "=", n * i)


# ======================================================
# 5. print a 3x3 grid of stars using nested loops
#    expected output:
#    * * *
#    * * *
#    * * *
# ======================================================
# n=3
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()


# ======================================================
# 6. print sum of 1 to n using while loop (n from input)
#    input.txt: 5
#    expected output: 15
# ======================================================
# n = int(input())
# i = 1
# res=0
# while i <= n:
#   res+=i
#   i += 1
# print(res)


# ======================================================
# 7. print only odd numbers from 1 to n (n from input)
#    input.txt: 10
#    expected output:
#    1 3 5 7 9
# ======================================================
n = int(input())
for i in range(1, n+1):
  if i % 2 != 0:
    print(i, end=" ")