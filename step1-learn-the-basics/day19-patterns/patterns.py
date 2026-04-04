import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Pattern 13
    """
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    """
    def pattern13(self, N):
        num = 1
        for i in range(1, N+1):
            for j in range(1, i+1):
                print(num, end=" ")
                num = num + 1
            print()
            
    # Pattern 14
    """
    A
    AB
    ABC
    ABCD
    ABCDE
    """
    def pattern14(self, N):
        for i in range(1, N+1):
            for j in range(1, i+1):
                print(chr(64+j), end="")
            print()
            
    # Pattern 15
    """
    ABCDE
    ABCD
    ABC
    AB
    A
    """
    def pattern15(self, N):
        for i in range(N, 0, -1):
            for j in range(1, i+1):
                print(chr(64+j), end="")
            print()
            
    # Pattern 16
    """
    A
    BB
    CCC
    DDDD
    EEEEE
    """
    def pattern16(self, N):
        for i in range(1, N+1):
            for j in range(1, i+1):
                print(chr(64+i), end="")
            print()
            
    # Pattern 17
    """
    A
   ABA
  ABCBA
 ABCDCBA
    """
    def pattern17(self, N):
        pass
 
if __name__ == "__main__":
    sol = Solution()
    N = n
    # sol.pattern13(N)
    # sol.pattern14(N)
    # sol.pattern15(N)
    sol.pattern16(N)
    # sol.pattern17(N)