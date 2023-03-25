# Написать функцию clean_string, которая получает строку и обрабатывает ее следующим образом:
# каждый символ # воспринмается как backspace, т.е. символ до # будет удален.
#
# Примеры:
# clean_string("abc#d##c") ==> "ac"

import traceback


def clean_string(s):
    stack = []
    for c in s:
        if c == '#':
            if stack:
                stack.pop()
        else:
            stack.append(c)
    if '#' in ''.join(stack):
        clean_string(''.join(stack))
    return ''.join(stack)


# Тесты
try:
    assert clean_string("abc#d##c") == "ac"
    assert clean_string("abc####d##c#") == ""
    assert clean_string("########") == ""
    assert clean_string("ab#cde##fgh#ij##") == "acfg"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
