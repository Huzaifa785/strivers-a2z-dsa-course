import sys
input = sys.stdin.readline

# number hashing inputs
# n = int(input())
# arr = list(map(int, input().split(" ")))
# q = int(input())

# string hashing inputs
s = input().strip() # added .strip() to get rid of the newlines and whitespaces
q = int(input())

class Solution:
    # Basic Number Hashing
    def number_hashing(self):
        # create hash array (size depends on max value)
        hash_arr = [0] * 13  # max number 12

        # precompute
        for num in arr:
            hash_arr[num] += 1

        # queries
        for _ in range(q):
            number = int(input())
            print(hash_arr[number])

    # Basic Character Hashing
    def char_hashing(self):
        # # lower case a to z
        # hash_arr = [0] * 26
        
        # ord_a = ord('a')

        # # precompute
        # for c in s:
        #     hash_arr[ord(c) - ord_a] = hash_arr[ord(c) - ord_a] + 1

        # # queries
        # for _ in range(q):
        #     c = input().strip()
        #     print(hash_arr[ord(c) - ord_a])

        # # upper case A to Z
        # hash_arr = [0] * 26
        
        # ord_A = ord('A')

        # # precompute
        # for c in s:
        #     hash_arr[ord(c) - ord_A] = hash_arr[ord(c) - ord_A] + 1

        # # queries
        # for _ in range(q):
        #     c = input().strip()
        #     print(hash_arr[ord(c) - ord_A])

        # all 256 characters
        hash_arr = [0] * 256
        print(len(hash_arr))
        
        # ord_A = ord('A')

        # precompute
        for c in s:
            hash_arr[ord(c)] = hash_arr[ord(c)] + 1

        # queries
        for _ in range(q):
            c = input().strip()
            print(hash_arr[ord(c)])


if __name__ == "__main__":
    sol = Solution() 

    # sol.number_hashing()
   
    sol.char_hashing()
