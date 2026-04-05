import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Pattern 17
    """
    A
   ABA
  ABCBA
 ABCDCBA
    """
    def pattern17(self, N):
        for i in range(1, N+1):
            for _ in range(N-i, 0, -1):
                print(" ", end="")
                
            ch = 'A'
            breakpoint = (i*2-1) // 2
            for j in range(i*2-1):
                print(ch, end="")

                if j < breakpoint:
                    ch = chr(ord(ch) + 1)
                else:
                    ch = chr(ord(ch) - 1)
                    
            print()
            
            # Pattern 18
    """
    E
    D E
    C D E
    B C D E
    A B C D E   
    """
    def pattern18(self, N):
        pass
 
if __name__ == "__main__":
    sol = Solution()
    N = n
    sol.pattern17(N)
    # sol.pattern18(N)