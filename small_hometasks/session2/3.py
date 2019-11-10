def user_split(line):
    lst = []
    i = 0
    while i < len(line):
        temp = ''
        while i < len(line) and line[i] == ' ':
            i += 1
        while i < len(line) and line[i] != ' ':
            temp += line[i]
            i += 1
        if len(temp) != 0:    
            lst += [temp]
    return lst 