# Написать функцию check_brackets, которая определяет правильно ли расставлены скобки () {} [] <> в предложении
#
# Примеры:
# camel_to_snake("(abc)[]{0:1}") ==> True
# camel_to_snake("(abc)]{0:1}[") ==> False

import traceback


def check_brackets(s):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for c in s:
        if c in brackets:
            stack.append(c)
        elif c in brackets.values():
            if not stack or brackets[stack.pop()] != c:
                return False
    return not stack


# Тесты
try:
    assert check_brackets('(5+5)/[4+4]*{2*2}') == True
    assert check_brackets('(3+[2*3)]') == False
    assert check_brackets('[{([[[<>]]])(<>)(){}}]') == True
    assert check_brackets(']()(){<>}[[()]]') == False
    assert check_brackets('[(sjd),"2"],{2:3}, [<>]') == True
    assert check_brackets('{[[[[((()))]]<]>]}') == False
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
