class Solution:
    def getLeastNumbers(self, arr, k: int):
        if len(arr) <= k:
            return arr

        def partition(first, end):
            if first > end:
                return 
            i, j = first, end
            while i < j:
                while i < j and arr[i] <= arr[j]:
                    j -= 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                while i < j and arr[i] <= arr[j]:
                    i += 1
                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]
                    j -= 1
            return i
        
        def quicksort(first, end):
            if first < end:
                pivot = partition(first, end)
                quicksort(first, pivot - 1)
                quicksort(pivot + 1, end)
        
        quicksort(0, len(arr) - 1)

        return arr[:k]