def split_by_indexes(line, ind_lst):
    ind_lst.sort()
    res_ind_lst = []
    for i in ind_lst:
        if i in range(1, len(line) + 1) and i not in res_ind_lst:
            res_ind_lst += [i]
    if not len(line) in res_ind_lst:
        res_ind_lst += [len(line)]
    lst = []
    j = 0
    for i in res_ind_lst:
        lst += [line[j:i]]
        j = i
    return lst