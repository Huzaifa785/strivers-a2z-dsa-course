import sys
input = sys.stdin.readline


# ======================================================
# 1. take two numbers on the same line, print their sum
#    input.txt: 3 7
#    expected output: 10
# ======================================================
# num1, num2 = map(int, input().split())
# res = num1 + num2
# print(res)


# ======================================================
# 2. take n, then n numbers on next line, print the largest
#    input.txt:
#    5
#    4 1 9 2 6
#    expected output: 9
# ======================================================
# n = int(input())
# n_nums = list(map(int, input().split()))
# print(max(n_nums))



# ======================================================
# 3. take a full sentence, print it reversed word by word
#    input.txt: hello world foo
#    expected output: foo world hello
# ======================================================

# =============== my solution ===============
# sentence = input().split()
# length_of_sentence = len(sentence)
# for _ in range(length_of_sentence - 1, -1, -1):
#     print(sentence[_], end=" ")
    
# =============== pythonic way ===============
sentence = input().split()
print(*sentence[::-1])


# ======================================================
# 4. take t test cases, each has two numbers, print their product
#    input.txt:
#    3
#    2 5
#    3 4
#    6 1
#    expected output:
#    10
#    12
#    6
# ======================================================
# t = int(input())

# for _ in range(t):
#     num1, num2 = map(int, input().split())
#     print(num1 * num2)
    


# ======================================================
# 5. take n numbers, print only the even ones
#    input.txt:
#    6
#    1 2 3 4 5 6
#    expected output: 2 4 6
# ======================================================

# =============== my solution ===================
# n = int(input())
# nums = list(map(int, input().split()))

# for i in range(n):
#     if nums[i] % 2 == 0:
#         print(nums[i], end=" ")

# ============== better way ===================
# n = int(input())
# nums = list(map(int, input().split()))

# for num in nums:
#     if num % 2 == 0:
#         print(num, end=" ")