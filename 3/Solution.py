class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        element_set = set()
        start_pos, end_pos = 0, 0
        while end_pos < len(s):
            if s[end_pos] not in element_set:
                element_set.add(s[end_pos])
                end_pos += 1
            else:
                max_len = end_pos - start_pos if max_len < end_pos - start_pos else max_len
                start_pos += 1
                end_pos = start_pos
                element_set.clear()
        # 计算最后一段的字串长度
        size = len(element_set)
        max_len = size if max_len < size else max_len

        return max_len


s = "dvdf"
mytest = Solution()
result = mytest.lengthOfLongestSubstring(s)
print(result)
