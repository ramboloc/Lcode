from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # 用于存储上级目录的列表
        lst = []
        cur = 'Main'

        for i in logs:
            if i == '../':
                cur = lst.pop() if len(lst) > 0 else cur
            elif i == './':
                cur = cur
            else:
                lst.append(cur)
                cur = i
        return len(lst)


logs = ["d1/", "d2/", "../", "d21/", "./"]
mytest = Solution()
print(mytest.minOperations(logs))
