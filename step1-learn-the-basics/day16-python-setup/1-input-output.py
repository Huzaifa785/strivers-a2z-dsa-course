import sys
input = sys.stdin.readline  # faster input, use this always in dsa/cp


# ======================================================
# 1. basic output
# ======================================================
# print("hello world")


# ======================================================
# 2. basic input - reading a number
# ======================================================
# x = int(input())
# print("hey", x)


# ======================================================
# 3. reading two numbers on separate lines
# ======================================================
# x = int(input())
# y = int(input())
# print(x, y)


# ======================================================
# 4. reading two numbers on the SAME line (e.g. "3 5")
# ======================================================
# x, y = map(int, input().split())
# print(x, y)


# ======================================================
# 5. reading a full line of text (like getline in c++)
# ======================================================
# line = input().strip()   # .strip() removes the trailing newline
# print(line)


# ======================================================
# 6. print on separate lines using \n and end=
# ======================================================
# x = int(input())
# y = int(input())
# print(x)
# print(y)
# print(x, y, sep="\n")   # same result, sep replaces the space between values


# ======================================================
# 7. reading a list of numbers on one line (e.g. "1 2 3 4 5")
# ======================================================
# nums = list(map(int, input().split()))
# print(nums)


# ======================================================
# 8. reading n numbers into a list (n given first)
# ======================================================
n = int(input())
nums = list(map(int, input().split()))
print(nums)


# ======================================================
# 9. print without newline at end (like cout without endl)
# ======================================================
# print("hello", end=" ")
# print("world")   # prints: hello world  (on same line)


# ======================================================
# uncomment one section at a time and set input.txt accordingly
# ======================================================
