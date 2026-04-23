import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Sum of first N numbers (parametrised)
    def solution1(self, i, sum, N):
        if i > N:
            print(sum)
            return
        self.solution1(i+1, sum+i, N)

    # Sum of first N numbers (functional way)
    def solution2(self, N):
        if N == 0:
            return 0
        
        return N + self.solution2(N-1)
    
    # Factorial of a number
    def solution3(self, N):
        if N == 0:
            return 1
        
        return N * self.solution3(N-1)


if __name__ == "__main__":
    sol = Solution() 
    N = n

    # sol.solution1(1, 0, N)

    # print(sol.solution2(N))

    print(sol.solution3(N))