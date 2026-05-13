import sys
from collections import defaultdict

input = sys.stdin.readline

# inputs
n = int(input())
arr = list(map(int, input().split(" ")))

class Solution:
    # selection sort
    def selection_sort(self, N, arr):
        for i in range(N-1):
            mini = i
            for j in range(i+1, N):
                if arr[j] < arr[mini]:
                    mini = j

            arr[i], arr[mini] = arr[mini], arr[i]

        print(arr)
            
        
if __name__ == "__main__":
    sol = Solution() 
    N = n
    my_arr = arr
    sol.selection_sort(N, my_arr)