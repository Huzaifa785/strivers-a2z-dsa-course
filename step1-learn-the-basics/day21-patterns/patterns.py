import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Pattern 18
    """
    E
    D E
    C D E
    B C D E
    A B C D E   
    """
    def pattern18(self, N):
        a_chr = 65
        chr_to_iterate = a_chr+N-1
        
        for i in range(1, N+1):
            for j in range(i):
                print(chr((chr_to_iterate-(i-j-1))), end=" ")
                
            print()
 
if __name__ == "__main__":
    sol = Solution()
    N = n
    sol.pattern18(N)