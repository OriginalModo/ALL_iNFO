def is_correct(seq):
    brackets = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i in seq:
        if i in brackets:
            if len(stack) == 0 or brackets[i] != stack[-1]:
                return False
            else:
                stack.pop()
        else:
            stack.append(i)
    return len(stack) == 0

print('yes' if is_correct(input()) else 'no')


