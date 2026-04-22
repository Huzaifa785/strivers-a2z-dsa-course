import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Print Name N times using recursion
    def solution1(self, i, N):
        if i > N:
            return
        print("huzaifa")
        self.solution1(i+1, N)

    # Print 1 to N using Recursion
    def solution2(self, i, N):
        if i > N:
            return
        print(i, end=" ")
        self.solution2(i+1, N)

    # Print N to 1 using Recursion
    def solution3(self, i, N):
        if i < 1:
            return
        print(i, end=" ")
        self.solution3(i-1, N)


if __name__ == "__main__":
    sol = Solution() 
    N = n
    # sol.solution1(1,N)
    
    # sol.solution2(1,N)

    i = N
    sol.solution3(i, N)
    # OR #
    # sol.solution3(N, N)