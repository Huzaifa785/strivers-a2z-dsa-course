import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Problem 4: Armstrong Number
    def problem4(self, N):
        # approach 1
        # total = 0
        # num = N
        # power = 0

        # while (num > 0):
        #     num = num // 10
        #     power += 1

        # for i in str(N):
        #     total = total + (int(i)**power)
        
        # print(N==total)

        # approach 2
        total = 0
        num = N
        power = 0

        while (num > 0):
            num = num // 10
            power += 1

        num = N
        while (num > 0):
            last_digit = num % 10
            total = total + last_digit**power
            num = num // 10

        
        print(N==total)

    # ================================================ #

    # Problem 5: Print all divisors
    def problem5(self, N):
        # approach 1
        # divisors = []
        # for i in range (1, N+1):
        #     if N % i == 0:
        #         divisors.append(i)
        # print(divisors)

        # approach 2
        # divisors = []
        # import math
        # for i in range(1, (int(math.sqrt(N)))+1):
        #     if (N % i == 0):
        #         divisors.append(i)
        #         if ((N//i) != i):
        #             divisors.append(N//i)
        # divisors.sort()
        # print(divisors)

        # approach 3 (without in-built sqrt function)
        divisors = []
        i = 1

        while i * i <= N:
            if N % i == 0:
                divisors.append(i)
                
                if i != N // i:
                    divisors.append(N // i)
            
            i += 1

        divisors.sort()
        print(divisors)

    # Problem 6: Prime Number
    def problem6(self, N):
        # approach 1 
        divisors = []
        i = 1
        while i*i <= N:
            if N % i == 0:
                divisors.append(i)
                if ((N // i) != i):
                    divisors.append(N // i)
            i += 1
        divisors.sort()

        if len(divisors) == 2:
            print(True)
        else:
            print(False)

if __name__ == "__main__":
    sol = Solution() 
    N = n
    # sol.problem4(N)
    # sol.problem5(N)
    sol.problem6(N)