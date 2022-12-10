from ast import parse
def is_valid_variable_name(name):
    try:
        parse('{} = None'.format(name))
        return True
    except (SyntaxError, ValueError, TypeError):
        return False
print(is_valid_variable_name('X'))
print(is_valid_variable_name('123'))
print(is_valid_variable_name('for'))
print(is_valid_variable_name(''))
print(is_valid_variable_name(42))