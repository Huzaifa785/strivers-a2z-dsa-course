import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split(" "))

class Solution:
    # Problem 7: GCD/HCF
    def problem7(self, N1, N2):
        # approach 1
        # gcd = 1
        # for i in range(1, min(N1, N2)+1):
        #     if N1 % i == 0 and N2 % i == 0:
        #         gcd = i
        # print(gcd)

        # trying in a reverse manner
        # for i in range(min(N1, N2), 1, -1):
        #     if N1 % i == 0 and N2 % i == 0:
        #         print(i)
        #         break

        # approach 2 (optimal) - euclidean algorithm
        while N1 > 0 and N2 > 0:
            if N1 > N2:
                N1 = N1 % N2
            else:
                N2 = N2 % N1

            if N1 == 0:
                print(N2)
            else:
                print(N1)

if __name__ == "__main__":
    sol = Solution() 
    N1 = n1
    N2 = n2
    sol.problem7(N1, N2)