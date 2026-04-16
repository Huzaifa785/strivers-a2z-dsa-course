import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Problem 1: Count all digits of a number
    """
    Sample Input:
    7185

    Sample Output:
    4
    """
    def problem1(self, N):
        # approach 1

        # counter = 0
        # while (N > 0):
        #     counter = counter + 1
        #     N = N // 10
        # print(counter)

        # approach 2
        # count = len(str(N))
        # print(count)

        # approach 3
        import math
        if N == 0:
            print(1)
        else:
            count = int(math.log10(N)) + 1
            print(count)

    # Problem 2: Reverse a number
    """
    Sample Input:
    7185

    Sample Output:
    5817
    """
    def problem2(self, N):
        # approach 1
        # nums = ""
        # while(N > 0):
        #     last_digit = N % 10
        #     nums = nums + str(last_digit)
        #     N = N // 10
        # print(int(nums))

        # approach 2
        rev_num = 0
        while(N > 0):
            last_digit = N % 10
            rev_num = (rev_num * 10) + last_digit
            N = N // 10
        print(rev_num)

if __name__ == "__main__":
    sol = Solution() 
    N = n
    # sol.problem1(N)
    sol.problem2(N)