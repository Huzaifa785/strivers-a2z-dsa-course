import sys
input = sys.stdin.readline

n = int(input())

class Solution:
    # Pattern 20
    """
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
    """
    def pattern20(self, N):
        empty_space = N * 2 - 2
        for i in range(1, N*2-1 + 1):
            stars = i
            if (i > N):
                stars = 2 * N - i
            for j in range(1, stars+1):
                print("*", end=" ")

            for j in range(empty_space):
                print(" ", end=" ")

            for j in range(1, stars+1):
                print("*", end=" ")

            if i < N:
                empty_space = empty_space - 2
            else:
                empty_space = empty_space + 2
            print()

    # Pattern 21
    """
    * * * * *
    *       *
    *       *
    *       *
    * * * * * 
    """
    def pattern21(self, N):
        # ==== my first try =====
        # space = N - 2
        # for i in range(1, N+1):
        #     for j in range(1, N+1):
        #         if i == 1 or i == N:
        #             print("*", end=" ")
                    
        #         if (i != 1 and i != N) and (j == 1):
        #             print("*", end=" ")

        #     if (i != 1 and i != N):
        #         for j in range(space):
        #             print(" ", end=" ")

        #     if (i != 1 and i != N):
        #         for j in range(1):
        #             print("*", end=" ")
        #
        #    print()


        # === optimized solution ===
        for i in range(N):
            for j in range (N):
                if (i==0 or i==N-1 or j==0 or j==N-1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            print()

    # Pattern 22 (N=4)
    """
    4444444
    4333334
    4322234
    4321234
    4322234
    4333334
    4444444
    """
    def pattern22(self, N):
        for i in range(N*2-1):
            for j in range(N*2-1):
                top = i
                left = j
                right = (2 * n - 2) - j
                down = (2 * n - 2) - i
                print(N - min(min(top, down), min(left,right)), end=" ")
            
            print()

if __name__ == "__main__":
    sol = Solution()
    N = n
    # sol.pattern20(N)
    # sol.pattern21(N)
    sol.pattern22(N)