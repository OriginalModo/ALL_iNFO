from collections import deque


class Solution:
    def is_valid_new(self, s):
        stack = deque()
        open = ['(', '{', '[']
        match = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if match[last] != i:
                    return False
        if len(stack) == 0:
            return True
        return False


ss = Solution()

print(ss.is_valid_new('(){)'))
