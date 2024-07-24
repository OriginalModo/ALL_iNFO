def is_correct_brackets(text):
    stact = []
    mathc = {'(': ')', '[': ']', '{': '}'}
    for i in text:
        if i in ['(', '[', '{']:
            stact.append(i)
        elif not stact or mathc[stact.pop()] != i:
            return False
    return not stact


print(is_correct_brackets('{}()['))
print(is_correct_brackets('{}()[]'))
