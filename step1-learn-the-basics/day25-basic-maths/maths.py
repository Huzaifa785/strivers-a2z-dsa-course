import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Problem 3: Palindrome Number
    def problem3(self, N):
        # approach 1
        # num = abs(N)
        # rev_num = 0

        # while(num > 0):
        #     last_digit = num % 10
        #     rev_num = (rev_num*10) + last_digit
        #     num = num // 10

        # if N < 0:
        #     rev_num = str(rev_num) + "-"
        
        # if str(N) == str(rev_num):
        #     print(True)
        # else:
        #     print(False)

        # approach 2
        if N < 0:
            print(False)
        else:
            rev_num = 0
            num = N

            while (num > 0):
                last_digit = num % 10
                rev_num = (rev_num * 10) + last_digit
                num = num // 10

            print(N==rev_num)


if __name__ == "__main__":
    sol = Solution() 
    N = n
    sol.problem3(N)