def remember_result(func):
    last_res = None
    def wrap(*args):
        nonlocal last_res
        print(f'last result = "{last_res}"')
        last_res = func(*args)
    return wrap

@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f'Current result = "{result}"')
    return result