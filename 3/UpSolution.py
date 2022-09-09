class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 1
        # s为空
        if not s:
            return 0
        substring = s[0]
        # s[0]肯定重复，所以从s[1]开始
        for i in s[1:]:
            # 判断重复
            if i in substring:
                index = substring.find(i)
                # 截断以更新子串
                substring = substring[index + 1:]
            # 子串自增长
            substring += i
            # 更新长度
            if len(substring) > length:
                length = len(substring)
        return length


s = "dvdf"
mytest = Solution()
result = mytest.lengthOfLongestSubstring(s)
print(result)
