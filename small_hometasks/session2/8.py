def get_pairs(init_lst):
    res_lst = []
    if len(init_lst) == 1 or len(init_lst) == 0:
        return None
    temp = None
    for i in init_lst:
        if temp != None:
            res_lst += [tuple([temp, i])]
        temp = i    
    return res_lst