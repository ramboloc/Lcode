class Solution:
    def reorderSpaces(self, text: str) -> str:
        arr = text.split(' ')
        space_count = len(arr) - 1
        word_count,arr_space,remain = 0,0,0
        for i in arr:
            if i != "":
                word_count += 1
        if word_count == 0:
            return ' '*space_count
        elif word_count == 1:
            arr_space = 0
            remain = space_count
        else:
            arr_space = space_count // (word_count - 1)
            remain = space_count % (word_count - 1)

        result = ''
        for i in arr:
            if i != '':
                result += i + " " * arr_space
        return result[0:len(result) - arr_space] + remain * ' '


test = '   '
mytest = Solution()
print(mytest.reorderSpaces(test))
