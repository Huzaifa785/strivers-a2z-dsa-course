import sys
input = sys.stdin.readline

# reverse array input
n = int(input())
array_input = list(map(int, input().split(" ")))


class Solution:
    # Reverse an array 
    def solution1(self, i, arr, N):
        if i >= N//2:
            print(arr)
            return
        arr[i], arr[N-i-1] = arr[N-i-1], arr[i]
        self.solution1(i+1, arr, N)

    # String palindrome
    def solution2(self, N):
        print(N)

    # Fiibonacci series
    def solution3(self, N):
        print(N)
        


if __name__ == "__main__":
    sol = Solution() 
    N = n
    arr = array_input

    # sol.solution1(0, arr, N)

    sol.solution2(N)

    # sol.solution3(N)