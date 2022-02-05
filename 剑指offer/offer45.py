class Solution:
    def minNumber(self, nums) -> str:
        strs = [str(num) for num in nums]
        print(len(strs)-1)
        def partition(first, end):
            i = first
            j = end
            while i < j:
                while i < j and strs[i] + strs[j] <= strs[j] + strs[i]:
                    j -= 1
                if i < j:
                    strs[i], strs[j] = strs[j], strs[i]
                    i += 1
                while i < j and strs[i] + strs[j] <= strs[j] + strs[i]:
                    i += 1
                if i < j:
                    strs[i], strs[j] = strs[j], strs[i]
                    j -= 1
            return i

        def quicksort(first, end):
            if first < end:
                pivot = partition(first, end)
                quicksort(first, pivot-1)
                quicksort(pivot + 1, end)

        quicksort(0, len(strs) - 1)
        return ''.join(strs)            

sol = Solution()
print(sol.minNumber([3,30,34,5,9]))
