import sys
from collections import defaultdict

input = sys.stdin.readline

# number hashing inputs
n = int(input())
arr = list(map(int, input().split(" ")))

class Solution:
    # number hashing using dictionary
    def number_hashing(self):
        # # using normal dict
        # d = {}

        # # precompute
        # for num in arr:
        #     if num in d:
        #         d[num] += 1
        #     else:
        #         d[num] = 1

        # # queries
        # for _ in range(q):
        #     number = int(input())
        #     print(d.get(number, 0))

        # using defaultdict
        d = defaultdict(int)

        # precompute
        for num in arr:
            d[num] += 1

        # queries
        for _ in range(q):
            number = int(input())
            # print(d[number])
            # the reason i also wrote this below approach is because if you just do d[number] it'll automatically create a new unnecessary key that isn't required, and our dict size will keep on increasing, for test cases with fewer numbers, it's completely fine, but if the inputs are aroud 10^6 or so, then it'll be a problem hence it's good to be on the safer side and use the hybrid approach 
            print(d.get(number, 0))

    # solution 1: frequencies of elements in an array
    def solution1(self):
        # # using defaultdict
        # d = defaultdict(int)

        # # precompute
        # for num in arr:
        #     d[num] += 1

        # for k, v in d.items():
        #     print(k, v)

        # using python dict
        d = {}

        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        for k, v in d.items():
            print(k, v)


    # solution 2: highest occuring element in an array
    def solution2(self):
        # using defaultdict
        # d = defaultdict(int)

        # # precompute
        # for num in arr:
        #     d[num] += 1

        # max_freq = float('-inf')
        # min_freq = float('inf')

        # max_elem = None
        # min_elem = None

        # # fetch
        # for k, v in d.items():
        #     if v > max_freq:
        #         max_freq = v
        #         max_elem = k

        #     if v < min_freq:
        #         min_freq = v
        #         min_elem = k
        
        # print(max_elem,max_freq)
        # print(min_elem,min_freq)

        # approach 2
        d = defaultdict(int)

        # precompute
        for num in arr:
            d[num] += 1

        max_elem = max(d, key=d.get)
        min_elem = min(d, key=d.get)

        print(max_elem, d[max_elem])
        print(min_elem, d[min_elem])

        
if __name__ == "__main__":
    sol = Solution() 

    # sol.number_hashing()

    # sol.solution1()

    sol.solution2()