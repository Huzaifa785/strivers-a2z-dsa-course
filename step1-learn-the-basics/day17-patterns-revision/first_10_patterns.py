import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Pattern 1
    """
    *****
    *****
    *****
    *****
    *****
    """
    def pattern1(self, N):
        for _ in range(N):
            for _ in range(N):
                print("*", end="")
            print()
    
    # Pattern 2
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    """
    def pattern2(self, N):
        for i in range(1, N+1):
            for _ in range(i):
                print("*", end=" ")
            print()
    
    # Pattern 3
    """
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    """
    def pattern3(self, N):
        for i in range(1, N+1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()
             
    # Pattern 4
    """
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    """
    def pattern4(self, N):
        for i in range(1, N+1):
            for _ in range(i):
                print(i, end=" ")
            print()
            
    # Pattern 5
    """
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    def pattern5(self, N):
        for i in range(N, 0, -1):
            for _ in range(i):
                print("*", end=" ")
            print()
       
    # Pattern 6
    """
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
    """
    def pattern6(self, N):
        for i in range(N, 0, -1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()
        
    
    # Pattern 7
    """
    *
   ***
  *****
 *******
*********
    """     
    def pattern7(self, N):
        for i in range(1, N+1):
            for _ in range(N-i, 0, -1):
                print(" ", end="")
                
            for _ in range(i*2-1):
                print("*", end="")
                
            for _ in range(N-i, 0, -1):
                print(" ", end="")
            print()
            
    # Pattern 8
    """
    *********
     *******
      *****
       ***
        *
    """
    def pattern8(self, N):
        for i in range(N, 0, -1):
            for _ in range(N-i):
                print(" ", end="")
                
            for _ in range(i*2-1):
                print("*", end="")
                
            for _ in range(N-i):
                print(" ", end="")
            print()
        
    # Pattern 9
    """
    *
   ***
  *****
 *******
*********
*********
 ******* 
  *****
   ***
    *
    """
    def pattern9(self, N):
        self.pattern7(N)
        self.pattern8(N)
      
    # Pattern 10
    """
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    """ 
    def pattern10(self, N):
        # self.pattern2(N)
        # self.pattern5(N-1)
        for i in range(1, 2*N):
            stars = i
            
            if i>N:
                stars = 2*N-i
            
            for _ in range(stars):
                print("*", end="")
            print()

if __name__ == "__main__":
    sol = Solution()
    N = n
    # sol.pattern1(N)
    # sol.pattern2(N)
    # sol.pattern3(N)
    # sol.pattern4(N)
    # sol.pattern5(N)
    # sol.pattern6(N)
    # sol.pattern7(N)
    # sol.pattern8(N)
    # sol.pattern9(N)
    sol.pattern10(N)