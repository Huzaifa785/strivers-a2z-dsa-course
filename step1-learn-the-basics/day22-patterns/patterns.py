import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Pattern 19
    """
    **********

    ****  ****
    ***    ***
    **      **
    *        *
    *        *
    **      **
    ***    ***
    ****  ****

    **********  
    """
    def pattern19(self, N):
        for i in range(N):
            for _ in range(N-i):
                print("*", end="")
                
            for _ in range(i*2):
                print(" ", end="")
                
            for _ in range(N-i):
                print("*", end="")
                
            print()
                        
        # second half
        for i in range(N-1, -1, -1):
            for _ in range(N-i):
                print("*", end="")
                
            for _ in range(i*2):
                print(" ", end="")
                
            for _ in range(N-i):
                print("*", end="")
            
            print()

 
if __name__ == "__main__":
    sol = Solution()
    N = n
    sol.pattern19(N)