# def is_correct_brackets(s):
#     a_list = []
#     for i in s:
#         if i in ['(', '[', '{']:
#             a_list.append(i)
#         if len(a_list) <= 0:
#             return False
#         if i == ')' and a_list.pop() != '(':
#             return False
#     if len(a_list) == 0:
#         return True
#     return False
#
#
# print(is_correct_brackets('(((())))'))  # True
# print(is_correct_brackets('(((())'))  # False
# print(is_correct_brackets('())))'))  # False
# print(is_correct_brackets('((((){}[]{}[])))'))  # True
# print(is_correct_brackets('(){}[]{}[])))'))  # False
# print(is_correct_brackets('(){}[]{}[]'))  # True

def is_balanced(parens: str) -> bool:
    # Link: https://stackoverflow.com/a/73341167/
    parens_map ={'(':')','{':'}','[':']'}
    stack = []
    for paren in parens:
        if paren in parens_map:  # is open
            stack.append(paren)
        elif paren in parens_map.values():  # is close
            if (not stack) or (paren != parens_map[stack.pop()]):
                return False
    return not stack


print(is_balanced('(((())))'))  # True
print(is_balanced('(((())'))  # False
print(is_balanced('())))'))  # False
print(is_balanced('((((){}[]{}[])))'))  # True
print(is_balanced('(){}[]{}[])))'))  # False
print(is_balanced('(){}[]{}[]'))  # True
