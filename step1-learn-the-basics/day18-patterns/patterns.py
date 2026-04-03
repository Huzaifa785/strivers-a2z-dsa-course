import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Pattern 11
    """
    1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1
    """
    def pattern11(self, N):
        for i in range(1, N+1):
            start = None
            if i % 2 == 0:
                start = 0
            else:
                start = 1
            for j in range(i):
                print(start, end=" ")
                
                start = 1 - start
                
            print()
            
    # Pattern 12
    """
    1        1   
    12      21  
    123    321
    1234  4321
    1234554321
    """
    def pattern12(self, N):
        space = N*2-2
        # print(space)
        for i in range(1, N+1):
            for j in range(1, i+1):
                print(j, end="")
                
            for j in range(space, 0, -1):
                # print("inside loop before", space, end=" ")
                print(" ", end="")
            space = space - 2
            # print("inside loop after", space, end=" ")
                
            for j in range(i, 0, -1):
                print(j, end="")
            
            print()
 
if __name__ == "__main__":
    sol = Solution()
    N = n
    # sol.pattern11(N)
    sol.pattern12(N)