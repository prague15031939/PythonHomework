def get_digits(num):
    num = str(num)
    tpl = []
    for i in num:
        tpl += [int(i)]   
    return tuple(tpl)