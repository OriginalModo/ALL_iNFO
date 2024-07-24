def new_str(new_str: str):
    is_good = True
    stack = []
    for i in new_str:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack:
                is_good = False
                break
            open_backet = stack.pop()
            if open_backet == '(' and i == ')':
                continue
            if open_backet == '[' and i == ']':
                continue
            if open_backet == '{' and i == '}':
                continue
            is_good = False
            break
    if is_good and len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


print(new_str('[]'))
print(new_str('{}}}'))
print(new_str('())'))
print(new_str('[]()()()())'))
