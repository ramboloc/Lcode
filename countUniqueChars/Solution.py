# 基础版
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            left_pos, right_pos = -1, len(s)
            # 向左检查
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    left_pos = j
                    break
            # 向右检查
            for k in range(i + 1, len(s)):
                if s[k] == s[i]:
                    right_pos = k
                    break
            count += (right_pos - i) * (i - left_pos)

        return count


# mytest = Solution()
# print(mytest.uniqueLetterString("LEETCODE"))
test='LEETCODE'
for i in enumerate(test):
    print(i)
