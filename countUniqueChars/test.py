# 暴力解体法

def uniqueLetterString(s: str) -> int:
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp = s[i:j]
            count += countUniqueChars(temp)

    return count


def countUniqueChars(s: str):
    temp_dict: dict = {}
    count = 0
    for i in range(0,len(s)):
        if temp_dict.get(s[i]) is None:
            temp_dict[s[i]] = 0
        else:
            temp_dict[s[i]] = 1
    for j in temp_dict.items():
        if j[1] == 0:
            count += 1
    return count


test = 'LEETCODE'
t_lst = ['1', '111', '11', '11', 12]
print(uniqueLetterString(test))
