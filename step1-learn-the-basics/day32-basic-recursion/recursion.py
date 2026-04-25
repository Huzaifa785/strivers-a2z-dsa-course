import sys
input = sys.stdin.readline

# palindrome input
# n = list(input())

# finbonacci input
n = int(input())

class Solution:
    # String palindrome
    def solution2(self, i, N):
        # approach 1
        # if i >= len(N) // 2:
        #     print("".join(rev_arr))
        #     print("".join(N))
        #     if "".join(rev_arr) == "".join(N):
        #         return True
        #     else:
        #         return False
        
        # rev_arr[i], rev_arr[len(N)-i-1] = rev_arr[len(N)-i-1], rev_arr[i]
        # return self.solution2(i+1, N, rev_arr)

        # approach 2
        if i >= len(N)//2:
            return True
        if N[i] != N[len(N)-i-1]:
            return False
        return self.solution2(i+1, N)

    # Nth Fiibonacci Number
    def solution3(self, N):
        # # approach 1
        # if num1 == 0 and num2 == 1:
        #     nums.append(0)
        #     nums.append(1)

        # if len(nums) > N:
        #     return nums[N-1] + nums[N-2]
            
        # tmp = num1
        # num1 = num2
        # num2 = tmp + num1
        # nums.append(num2)
        # return self.solution3(N, num1, num2, nums)

        # approach 2
        if N <=1:
            return N
        return (self.solution3(N - 1) + self.solution3(N - 2))

if __name__ == "__main__":
    sol = Solution() 
    N = n

    # rev_arr = n.copy()
    # print(sol.solution2(0, N))

    # approach 1
    # nums = []
    # print(sol.solution3(N, 0, 1, nums))

    # approach 2
    print(sol.solution3(N))