def foo(init_list):
    res_list = []
    product = 1
    for i in init_list:
        product *= i
    for i in init_list:
        res_list += [int(product / i)]
    return res_list