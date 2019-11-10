def get_top_performers(filepath, number_of_top_students=5):
    
    with open(filepath, "r") as f:
        line_list = f.readlines()
        
    base_list = [line.strip().split(',') for line in line_list]    
    base_list.remove(base_list[0])
    
    base_list.sort(key = lambda item: float(item[2]), reverse = True)
    res_list = [base_list[i][0] for i in range(number_of_top_students)]
        
    return res_list

def get_old(filepath):
    
    with open(filepath, "r") as f:
        line_list = f.readlines()
        
    base_list = [line.strip().split(',') for line in line_list]
    temp = base_list[0]
    base_list.remove(base_list[0])
    
    base_list.sort(key = lambda item: int(item[1]), reverse = True)
    base_list.insert(0, temp)
    
    with open("D:\\py_temp\\old_man.csv", "w") as f:
        for item in base_list:
            f.write(item[0] + ',' + item[1] + ',' + item[2] + '\n')

    return 'success'