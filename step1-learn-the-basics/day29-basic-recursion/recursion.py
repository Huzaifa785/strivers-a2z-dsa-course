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

if __name__ == "__main__":
    sol = Solution() 
    N = n
    sol.solution1(1,N)