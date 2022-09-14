from typing import List


class Solution:
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        num = len(arr) // 20
        sum_arr = 0
        for i in range(num, len(arr) - num):
            sum_arr += arr[i]
        return sum_arr / (len(arr) - 2 * num)


logs = [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8,
        2, 3, 4]
mytest = Solution()
print(mytest.trimMean(logs))

