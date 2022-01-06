class Solution:
    def lastRemaining0(self, n: int) -> int:# overtime
        arr = list(range(1, n + 1, 1))
        def pop_element(arr, left):
            nn = len(arr)
            if len(arr) <= 1:
                return arr
            if left == 1:
                start = 0
                drop = 1
                adjust = 1
            else:
                start = len(arr) - 1
                drop = start - 2
                adjust = 0
            arr.pop(start)
            drop_count = 1
            while drop_count < nn/2:
                arr.pop(drop)
                drop += (2*left)
                drop -= adjust
                drop_count += 1
            return arr

        while len(arr) > 1:
            arr = pop_element(arr, 1)
            arr = pop_element(arr, -1)

        print(arr)

    def lastRemaining(self, n: int) -> int:
        def cal(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n % 2 == 1:
                return cal(n-1)
            else:
                return 2*(1+n/2-cal(n/2))
        return cal(n)

s = Solution()
s.lastRemaining(10)