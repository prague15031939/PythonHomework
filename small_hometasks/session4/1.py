with open("D:\\py_temp\\unsorted_names.txt", "r") as f:
    lines = sorted(f.readlines())
    
with open("D:\\py_temp\\sorted_names.txt", "w") as f:
    for line in lines:
        f.write(line)