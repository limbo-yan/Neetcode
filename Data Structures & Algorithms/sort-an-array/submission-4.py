class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heapSort(arr):
            n = len(arr)

            # build max heap
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            # extract elements one by one
            for j in range(n - 1, 0, -1):
                arr[0], arr[j] = arr[j], arr[0]
                heapify(arr, j, 0)

        heapSort(nums)
        return nums